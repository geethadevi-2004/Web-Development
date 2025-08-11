from django.db import models


# 1. Base Resume Info
class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    summary = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.name

# 2. Skills
class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.resume.name})"

# 3. Experience
class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company} ({self.resume.name})"

# 4. Projects
class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.resume.name})"

# 5. Achievements
class Achievement(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.resume.name})"
