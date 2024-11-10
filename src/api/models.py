from django.db import models
from django.utils.text import slugify

# Create your models here.
class Term(models.Model):
    name = models.CharField(max_length=15)
    year = models.CharField(max_length=7)
    handle = models.SlugField(default='',max_length=25)

    def get_url(self):
        return self.handle

    def __str__(self):
        return f"{self.name} {self.year}"

#UPDATED 
class Kid(models.Model):
    class ClassChoices(models.TextChoices):
        DAYCARE  = "Daycare"
        NURSERY = "Nursery"

    term = models.ForeignKey(Term,on_delete =models.CASCADE)
    full_name = models.CharField(max_length=50)
    handle = models.SlugField(max_length=50,default='')
    age = models.CharField(max_length=2)
    parent_first_contact = models.CharField(max_length=11)
    parent_second_contact = models.CharField(max_length=11,blank=True,null=True)
    kid_class = models.CharField(max_length=7,
                                 choices = ClassChoices.choices,
                                 default=ClassChoices.NURSERY)

    kid_picture = models.ImageField(blank = True,
            upload_to = "kids_image_gallery",
            null = True)
    class Meta:
        ordering = ('-full_name',)

    def save(self,*args,**kwargs):
        if not self.handle:
            self.handle = slugify(self.full_name)
        super().save(*args,**kwargs)
    
    def get_url(self):
        return self.handle

    def __str__(self):
        return self.full_name

class Payment(models.Model):
    class Payment_For_Choices(models.TextChoices):
        BOOKS = "Book"
        SCHOOL_FEES = "School Fees"
        MONTHLY_FEE = "Monthly Fee"

    class Payment_Type(models.TextChoices):
        PART_PAYMENT = "Part Payment"
        COMPLETE_PAYMENT  = "Complete Payment"

    kid = models.ForeignKey(Kid,on_delete = models.CASCADE)
    payment_for = models.CharField(max_length=11,
                                   choices = Payment_For_Choices.choices,
                                   default = Payment_For_Choices.SCHOOL_FEES)

    term_paid_for = models.ForeignKey(Term,on_delete = models.CASCADE)

    payment_type = models.CharField(max_length=16,
                                    choices = Payment_Type.choices,
                                    default = Payment_Type.COMPLETE_PAYMENT)

    amount = models.IntegerField()
    handle = models.SlugField(default='')

    paid_on = models.DateField()

    class Meta:
        ordering = ('-paid_on',)

    def save(self,*args,**kwargs):
        if not self.handle:
            self.handle = slugify(self.kid,self.amount)
        super().save(*args,**kwargs)

    def get_url(self):
        return self.handle

    def __str__(self):
        return f"{self.payment_type} of N{self.amount} for {self.payment_for} on {self.paid_on} by {self.kid}"
