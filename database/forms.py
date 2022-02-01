from database.models import class_stu_tech
from django import forms
from django.core.validators import RegexValidator

class_stu_tech_choices =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
    ("6" , "Six"),
    ("7" , "Seven"),
    ("8" , "Eight"),
    ("9" , "Nine"),
    ("10" , "Ten"),
    ("11" , "Eleven"),
    ("12" , "Twelve"),
)


name_REGEX=RegexValidator(r'/^[A-Za-z\s]+$/' , "Enter the correct Name")
username_REGEX=RegexValidator(r'.*' , "Enter the Username")
pwd_REGEX=RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$' , "Enter the password which contains atleast one upper cas one lowercase letter , atleast one number , one special character , and is of minimum length 8")

class stu_sign_up(forms.Form):
    name = forms.CharField(required=True , label="stu_name" , help_text="Eg. Suhani Bajpai" , error_messages="Invalid Name" , validators=[name_REGEX])
    username = forms.CharField(required=True , label="stu_username" , help_text="Eg. Suhani_4" , error_messages="Enter some other username" , validators=[username_REGEX])
    password = forms.CharField(required=True , label="stu_pwd" , error_messages="Enter the pwd acc to the instructions" , validators=[pwd_REGEX])
    confirm_password= forms.CharField(required=True , label="stu_con_pwd" , error_messages="Does not match with pwd" , validators=)
    class_stu = forms.ChoiceField(required=True , label="stu_class" , validators= )
    email_id = forms.EmailField(required=True , label="stu_email_id" , help_text="suhani.bajpai.cse20@itbhu.ac.in" , error_messages="Invalid Email-ID" , validators=)
    mobile_no = forms.IntegerField(required=True , label="stu_mobile_no" , error_messages="Invalid Mobile Number" , validators=)
    subjects_availed = forms.MultipleChoiceField(required=True ,label="stu_subejcts_availed", validators=)

    def clean(self):

        # data from the form is fetched using super function
        super(stu_sign_up, self).clean()

        name=self.cleaned_data.get('name')
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        class_stu=self.cleaned_data.get('class_stu')
        email_id=self.cleaned_data.get('email_id')
        mobile_no=self.cleaned_data.get('mobile_no')
        subjects_availed=self.cleaned_data.get('subjects_availed')

        if(password!=confirm_password):
            self._errors['password'] = self.error_class(["Confirm passwrod field must match with password field"])

        regex="/^[A-Za-z\s]+$/"

        return self.cleaned_data

