from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm, SkillFormSet, ExperienceFormSet, ProjectFormSet, AchievementFormSet
from .models import Resume, Skill, Experience, Project, Achievement
from django.template.loader import render_to_string
from django.conf import settings
import pdfkit


# Home Page
def home(request):
    return render(request, 'home.html')


# Helper function to assign resume to formset instances and save
def assign_and_save_formset(formset, resume):
    instances = formset.save(commit=False)
    for instance in instances:
        instance.resume = resume
        instance.save()
    # Handle deletions if user removed any forms
    for obj in formset.deleted_objects:
        obj.delete()


# Resume Form View (Add/Build)
def build_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)  # ✅ FIXED
        skill_formset = SkillFormSet(request.POST, prefix='skill')
        experience_formset = ExperienceFormSet(request.POST, prefix='experience')
        project_formset = ProjectFormSet(request.POST, prefix='project')
        achievement_formset = AchievementFormSet(request.POST, prefix='achievement')

        if all([
            form.is_valid(),
            skill_formset.is_valid(),
            experience_formset.is_valid(),
            project_formset.is_valid(),
            achievement_formset.is_valid()
        ]):
            resume = form.save()
            assign_and_save_formset(skill_formset, resume)
            assign_and_save_formset(experience_formset, resume)
            assign_and_save_formset(project_formset, resume)
            assign_and_save_formset(achievement_formset, resume)

            return redirect('preview_resume', resume.id)

    else:
        form = ResumeForm()
        skill_formset = SkillFormSet(queryset=Skill.objects.none(), prefix='skill')
        experience_formset = ExperienceFormSet(queryset=Experience.objects.none(), prefix='experience')
        project_formset = ProjectFormSet(queryset=Project.objects.none(), prefix='project')
        achievement_formset = AchievementFormSet(queryset=Achievement.objects.none(), prefix='achievement')

    return render(request, 'build_resume.html', {
        'form': form,
        'skill_formset': skill_formset,
        'experience_formset': experience_formset,
        'project_formset': project_formset,
        'achievement_formset': achievement_formset,
    })


# Resume Preview View
def preview_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    skills = Skill.objects.filter(resume=resume)
    experiences = Experience.objects.filter(resume=resume)
    projects = Project.objects.filter(resume=resume)
    achievements = Achievement.objects.filter(resume=resume)

    return render(request, 'preview_resume.html', {
        'resume': resume,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'achievements': achievements,
    })

