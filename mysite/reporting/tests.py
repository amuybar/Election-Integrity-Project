from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from .models import IncidentReport
from .forms import IncidentReportForm

class IncidentReportModelTest(TestCase):
    def setUp(self):
        self.incident = IncidentReport.objects.create(
            incident_type='voter_intimidation',
            location='Polling Station A',
            description='Voter was harassed while entering the polling station.',
            contact_info='john@example.com'
        )

    def test_incident_report_creation(self):
        self.assertTrue(isinstance(self.incident, IncidentReport))
        self.assertEqual(str(self.incident), "Voter Intimidation at Polling Station A")

    def test_incident_report_default_status(self):
        self.assertEqual(self.incident.status, 'pending')


class IncidentReportFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'incident_type': 'voter_intimidation',
            'location': 'Polling Station B',
            'date_time': timezone.now(),
            'description': 'Long wait times observed.',
            'contact_info': 'jane@example.com'
        }
        form = IncidentReportForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'incident_type': 'invalid_type',
            'location': '',
            'date_time': 'invalid_date',
            'description': 'Test description',
        }
        form = IncidentReportForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_evidence_file_size_validation(self):
        large_file = SimpleUploadedFile("large_file.jpg", b"0" * (10 * 1024 * 1024 + 1))  # 10MB + 1 byte
        form_data = {
            'incident_type': 'voter_intimidation',
            'location': 'Polling Station C',
            'date_time': timezone.now(),
            'description': 'Test description',
        }
        form = IncidentReportForm(data=form_data, files={'evidence': large_file})
        self.assertFalse(form.is_valid())
        self.assertIn('evidence', form.errors)

    def test_evidence_file_type_validation(self):
        invalid_file = SimpleUploadedFile("document.pdf", b"file_content")
        form_data = {
            'incident_type': 'voter_intimidation',
            'location': 'Polling Station D',
            'date_time': timezone.now(),
            'description': 'Test description',
        }
        form = IncidentReportForm(data=form_data, files={'evidence': invalid_file})
        self.assertFalse(form.is_valid())
        self.assertIn('evidence', form.errors)


class IncidentReportViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_report_incident_view_get(self):
        response = self.client.get(reverse('reporting:report_incident'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reporting/report_incident.html')
        self.assertIsInstance(response.context['form'], IncidentReportForm)

    def test_report_incident_view_post_valid(self):
        form_data = {
            'incident_type': 'voter_intimidation',
            'location': 'Polling Station E',
            'date_time': timezone.now(),
            'description': 'Test incident description',
            'contact_info': 'test@example.com'
        }
        response = self.client.post(reverse('reporting:report_incident'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(IncidentReport.objects.filter(location='Polling Station E').exists())

    def test_report_incident_view_post_invalid(self):
        form_data = {
            'incident_type': 'invalid_type',
            'location': '',
            'date_time': 'invalid_date',
            'description': 'Test description',
        }
        response = self.client.post(reverse('reporting:report_incident'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reporting/report_incident.html')
        self.assertFalse(response.context['form'].is_valid())

    def test_report_confirmation_view(self):
    incident = IncidentReport.objects.create(
        incident_type='voter_intimidation',
        location='Polling Station F',
        description='Test confirmation incident',
    )
    response = self.client.get(reverse('reporting:report_confirmation', args=[incident.id]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'reporting/report_confirmation.html')
    self.assertEqual(response.context['incident'], incident)
