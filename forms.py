from django import forms
from .models import Resume, Skill, Experience, Project, Achievement
from django.forms import modelformset_factory

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'linkedin', 'github', 'portfolio', 'summary','photo']

# ✅ Custom form for Experience with labels
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'duration', 'description']
        labels = {
            'title': 'Title',
            'company': 'Company',
            'duration': 'Duration',
            'description': 'Description'
        }

# Custom form for Achievement (optional if no description needed)
class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title']
        labels = {
            'title': 'Achievement'
        }

# ✅ FormSets
SkillFormSet = modelformset_factory(Skill, fields=('name',), extra=1, can_delete=True)
ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm, extra=1, can_delete=True)
ProjectFormSet = modelformset_factory(Project, fields=('title', 'link', 'description'), extra=1, can_delete=True)
AchievementFormSet = modelformset_factory(Achievement, form=AchievementForm, extra=1, can_delete=True)
