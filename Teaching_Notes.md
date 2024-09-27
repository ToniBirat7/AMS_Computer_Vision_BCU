## Project Planning

## Things to Consider

- While taking attendance, user might modify the id of the row using inspect element. How will you handle it?
- About ASGI and WSGI
- In the `auth` app except login and admin other pages are complex for making simple
  frontend.

## Git Hub (How to Merge)

- Checkout to the directory that you want to merge the files to
- `git fetch origin`
- `git merge main`
- git commit -m "Merged main into branch name"
- git push origin branch-name

# **Week 1 (2081-04-20 to 04-25)**

### **04-20**

- ## **Tasks**

  - [x] Project Features (with Demo)

    - [x] Admin and Teacher Login
    - [x] CRUD Operation for Admin
    - [x] Calender
    - [x] Attendance
    - [x] Profile

      - [x] Add / Remove Profile Photo
      - [x] Edit Personal Details

  - [x] Explore Templates and Static Files

  - [x] Git and Github and Project Initialization

  - [x] Setting Virtual Environment with Specific Python Version

    - [x] What is Virtual Environment?
    - [x] How to activate?
    - [x] Folder Structure
    - [x] How to deactivate?

  - [x] Starting Django Project

    - [x] Setup Setting File

      - [x] Template Location
      - [x] Static Location

    - [x] Create auth app
    - [x] Set urls
    - [x] Understand the project structure

  - [x] Create Github Collaboration

    - [x] Create branch for each member
    - [x] Clone the project with all the default templates
    - [x] Checkout to your branch

### **04-21**

- ## **Task (For Login and Admin Page)**

  - [x] Request Response Cycle (Working of Django)

    - [x] Making Request (GET,POST)
    - [x] WSGI
    - [x] Middleware
    - [x] URL Resolver
    - [x] Interaction with View
    - [x] Response

  - [x] Login Page

          - [x] Login Page HTML + CSS Code Explanation. Explain what each tag is doing? How CSS is working? Try removing and adding tags and css.
          - [x] Why do we use DTL to link static files?

            - We are currently in Development phase, during this phase the static files are served using `static` folder. But in the production static files are served differently by webserver like `nginx`by making a separate static folder using `collectstatic` or static files are served from a different location e.g `CDN`. For example, bootstrap is served using CDN because the CSS files are not in our computer but they are taken from CDN server.

          - [x] How static URL is set for the static pages? Explain everything in detail. Why did we use `STATIC_URL` in the `settings.py`.

  - [x] Why use DTL tags? Explain with Example.

    - We cannot write login in HTML. For that Django uses DTL.
    - Use DTL in the login page.

  - [x] DTL (Variables, Tags and Filters)

    - [x] Tag
      - Tags are used to write logic. For loop, conditional.
      - Some tags require ending tags too. Example : `{%for i in names%}} {% endfor %}`
      - `Syntax : {%  %}`
    - [x] Filter
      - There are in built filters. We can also make custom filter.
      - Function. Take input and gives output.
      - `{{ var_name|filter }}`
    - [x] Comment
      - `{% comment %} {% endcomment %}`

  - [x] Use `{% load static %}` : It loads the `static` template tag.

    - Use of `{% static 'login.css' %}` tag : Used to generate correct url for the static files. We can avoid hard coded URLs in the template. It gives us flexibility since changes to the static files configuration(like `STATIC_URL`) will be seen on the template without error.
    - `STATICFILES_DIRS` : Path for Django to look for static files.

  - [x] Create a normal form. Difference between `forms.form`, `modelForm` and `frontendForm` with Advantage and Disadvantage.

    - **Normal**
      - Username Form : `<input type="text" name="username" class="input" maxlength="150" placeholder="Enter Username" required="" id="id_username">`
      - Password Form : `<input type="password" name="password" class="input" maxlength="30" placeholder="Enter Password" required>`

  - [x] Explain all the forms with code with example.
  - [x] GET and POST request

    - HTTP Request : Whenever we sent a request we are sending the below plain text to the server.

      - GET

        ````http
        GET /login HTTP/1.1
        Host: http://127.0.0.1:8000/
        User-Agent: Chrome/58.0.3029.110 Safari/537.36
        Accept: text/html
        Accept-Language: en-US```

        ````

      - POST

        - POST : A POST request is one of the most common HTTP methods used by web clients (such as browsers) to send data to a server.

      - Data is sent in the body

        ````http
        POST /login HTTP/1.1 // Request Line

        // Request Headers
        Host: http://127.0.0.1:8000/
        User-Agent: Chrome/58.0.3029.110
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 37
        Accept: text/html
        Accept-Language: en-US

        // Body
        username=johndoe&password=secretpassword```

        - Here content-type is for encoding. Suppose we have special characters like `+` it is encoded into `%2B` and `&` into `%26`
        ````

    - HTTP Response : Whenever we sent a request we are sending the below plain text to the server.

      - GET Response

        ```
        HTTP/1.1 200 OK // Response Line with Status Code
        Content-Type: text/html
        Content-Length: 137

        // Body
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Form Submission Successful</title>
        </head>
        <body>
            <h1>Thank you for your submission!</h1>
        </body>
        </html>
        ```

  - [x] Form Submission. Explain about Method and Action.
    - Use the inspect window to visualize the Request and Response
  - [x] Display Request Object
    - Use `print(dir(request))`
  - [x] CSRF Token
  - [x] Handle Get and Post Request in the`Views`
  - [x] Create Superuser (Tables in DB SQ Lite)
  - [x] Migrations and Migrate to DB

- [x] Push the work in the respective branch

### **04-22**

- ## **Tasks**

  - [x] Task to do : Decorate the Warning Message.
  - [x] Messages in Django : Notification Features uses Message

    - Used to give feedback to the users.

    - SUCCESS
    - Warning
    - Info

      ```
        {% if messages %}
        {% for message in messages %}
        <h1>
            <p> You Have Received {{ message }} {{ message.tags}}</p>
        </h1>
        {% endfor %}
        {% endif %}
      ```

  - [x] Create a normal form. Difference between `forms.form`, `modelForm` and `frontendForm` with Advantage and Disadvantage.

    - **froms.form**

      - We can create forms in 3 different ways. Normal, forms.form, ModelForm
      - It is better to use Django forms because it has many features such as error generating and backend validation. For e.g. we can give error for specific element.
      - Create forms.py

        ```python
        from django import forms

        class LogForm(forms.Form):
          username = forms.CharField(
          widget=forms.TextInput(attrs={
              'class': 'input',
              'maxlength': "30",
              'placeholder': 'Enter Username'
              }),
          error_messages={'required': "Username can't be empty"}
          )
          password = forms.CharField(
            widget=forms.PasswordInput(attrs={
            'class': 'input',
            'maxlength': "30",
            'placeholder': 'Enter Password'
            }),
          error_messages={'required': "Password can't be empty"}
          )
        ```

      - `forms.DataType(widget=forms.InputType(attrs={'att_name':'value'}))
      - Explain the forms field with widgets from documentation. `https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#built-in-widgets`

      - Print the form and explain for GET request
      - Pass it using context

  - [x] What is Context and Context Processor?

    - The concept of "context" and "context processors" is central to how data is passed from the view to the template, allowing dynamic rendering of web pages.

  - [x] Context

    - In Django, a context is a dictionary that contains data to be rendered in a template. When you render a template, you provide it with a context dictionary, and the template uses this data to produce the final HTML output.
    - Give Example

    ```python
      from django.shortcuts import render

      def example_view(request):
          context = {
              'username': 'Birat',
              'age': 25
          }
          return render(request, 'example_template.html', context)

      <h1>Welcome, {{ username }}!</h1>
      <p>You are {{ age }} years old.</p>
    ```

  - [x] Context Processor

        - Sometimes, there's information you want to include in every single template (like the website name, current year, or logged-in user). This is where context processors come in.

        - Context processors are functions that return a dictionary of variables to be merged into the context of every template. They are a way to inject common data into every template context without explicitly passing it in each view.

        - It's a function that automatically adds data to the `context` dictionary before it's passed to the template.

        - Go to settings templates to explain built in context processor.

          ```python
          django.template.context_processors.debug: Adds debug information if DEBUG is True.
          django.template.context_processors.request: Adds the request object to the context.
          django.template.context_processors.static: Adds the STATIC_URL setting to the context.
          django.template.context_processors.media: Adds the MEDIA_URL setting to the context.
          django.template.context_processors.csrf: Adds a CSRF token for security.
          ```
        - Show example of Context Processor

         ```python
            def login_page(request):
              if request.method == 'POST':
                  print(request.POST)
                  username = request.POST.get('username')
                  password = request.POST.get('password')
                  print("*******")
                  print(username,password)
                  user = authenticate(username=username, password=password)
                  print(user)
                  if user is None:
                      messages.warning(request, 'Invalid Username or Password')
                  else:
                      login(request, user)
              return render(request, 'auth/login.html')
         ```

          ```HTML
          {% if request.user.is_authenticated %}
          <p>Welcome, {{ request.user.username }}!</p>
          {% else %}
          <p>Please <a href="{% url 'login' %}">log in</a>.</p>
          {% endif %}
          ```

        - Here, we are using `request` context for every template.

        - To prove this cause some error.

        - Another example is, when we GET request a page which consist `{% csrf %}` how is it getting the token value? We haven't passed any info to the frontend to display (we have not used any DTL tag for csrf) but how is token being generated? It is done by context_process that gives token value from the backend to the frontend. Here, `{% csrf_token %}` is made available due to context processor.

  - [x] Handle POST request for Form

    ```python
      if request.method == 'POST':
          form = LogForm(request.POST)
          if form.is_valid():
              print(form.cleaned_data)
              username = form.cleaned_data.get('username')
              password = form.cleaned_data.get('password')
              user = authenticate(username=username, password=password)
              if user is None:
                  messages.warning(request, 'Invalid Username or Password')
              else:
                  print("User is authenticated")
      else:
          form = LogForm()
      print(form)
      return render(request, 'auth/login.html', {'form': form})
    ```

    - Passing `request.POST` in the form
    - Print the form after passing request.POST. You can pass it as `data=request.POST` also.
    - Describe `is_valid` and `form.cleaned_data`

      - **is_valid**
        - Go to the `is_valid` function definition to show.
        - Checks if the form is bound and does not contain any error. Form bound means if the fields contains data and checks for any validation error example max_length for each form field.
        - If there are any errors in the form they are stored in the `form.errors`
        - Print `form.errors`

    - Print `form.cleaned_data` it is a dictionary.
      - All the values after `is_valid` are completed are stored inside `cleaned_data` attribute.

### **04-23**

- **Tasks**

  - Till now we are only relying on frontend validation

  - [x] Frontend Validation vs Backend Validation

            - Suppose you submitted a form now you want to check if the password contains valid characters. For example while creating an account we are made to input combination of characters. For this html form cannot validate all the things. So we have to use custom validation. So this is the advantage of forms.

            - Another example is if the username contains space or for password.

            - Then create a function to validate these things. This should be after `POST` request handling.

              - **clean_fieldname**

                - Django allows you to define a custom clean method for any field in the form by following the naming convention `clean_<fieldname>`. If there are error then raise the error for that field else return the valid field back to `cleaned_data`
                - After the error is raised it is stored in the `forms.error` print it to display the error in the console.

                ```python
                  class LogForm(forms.Form):
                    username = forms.CharField(
                        widget=forms.TextInput(attrs={
                            'class': 'input',
                            'maxlength': "30",
                            'placeholder': 'Enter Username'
                        }),
                        error_messages={'required': "Username can't be empty"}
                    )
                    password = forms.CharField(
                        widget=forms.PasswordInput(attrs={
                            'class': 'input',
                            'maxlength': "30",
                            'placeholder': 'Enter Password'
                        }),
                        error_messages={'required': "Password can't be empty"}
                    )

                    def clean_username(self):
                        username = self.cleaned_data.get('username')
                        if ' ' in username:
                            raise forms.ValidationError("Username should not contain spaces")
                        return username

                    def clean(self):
                        cleaned_data = super().clean()
                        password = cleaned_data.get('password')
                        # Additional custom validation can be done here
                        if ' ' in password:
                          raise forms.ValidationError("Space are not allowed")

                        return cleaned_data
                ```

              - `Use {{form.username.errors}}` to display the error.

            - **clean**

              - It is used if we have
              - The `clean` method of a form is used for form-wide validation, which can involve multiple fields. As we are inheriting `form.Form` we have `clean` method of `Form` which inherits `BaseForm` class inside which we have `clean` method.
              - `clean` method returns the initially `cleaned_data` which can be checked further for advance field validation.
              - `super().clean()` is called to ensure that the parent class’s clean method is executed, which performs basic validation for all fields and populates `self.cleaned_data` with cleaned values.
              - If the validation passes then it is stored inside `cleaned_data` else raises error for that field.
              - Display the password error in html.
              - Note : The validation using `clean` method is stored inside non field errors. Therefore, to display them

                ```python
                  {% if form.non_field_errors %}
                      <div class="error">
                          {% for error in form.non_field_errors %}
                              <p>{{ error }}</p>
                          {% endfor %}
                      </div>
                  {% endif %}
                ```

              - Form Initialization: When an instance of LogForm is created, the fields (username and password) are initialized with the specified widgets, attributes, and error messages.

              - Form Submission and Validation: When the form is submitted (usually via an HTTP POST request), Django processes the form data and calls the is*valid() method on the form instance.

            - Field-Level Validation: During this process, Django automatically calls any clean\*<fieldname> methods for individual fields, such as clean_username. This is where the username is validated against the custom rules defined in the clean_username method.

            - Form-Level Validation: After field-level validation, Django calls the clean() method to perform any additional form-wide validation. This is where the password is checked for spaces in the example.

            - Error Handling: If any ValidationError is raised during the field or form-level validation, the error message is added to the form’s error dictionary, which can then be accessed in the template to display error messages to the user.

    - When we use `raise form.ValidationError()` the `is_valid` function is `false`.
    - Get inside the `form` class to show `valid`.

  - Now we've valid credentials now what? We have to move the user to the next phase i.e. `redirect`

  - [x] Handle the authentication

    - `redirect(to, *args)` function

      - The redirect function in Django is used to redirect the user to a different URL. It is a convenient way to direct a user from one view to another after processing a request.
      - When you call redirect, Django sends an HTTP response with a status code of `302` (Found) or `301` (Moved Permanently), depending on whether the permanent argument is `True` or `False`. This status code tells the browser to make a new request to the specified URL.
      - We can also, redirect to other URL, for example : `return redirect('https://www.youtube.com/')`
      - Here we've to change the URL so we cannot use `render` because render is used to display template. If we use `render` the URL won't change.
      - If to is the name of a view or a URL pattern, Django will reverse the URL using the `reverse()` function, which converts the `view name` to a URL.
      - Once the target URL is determined, `redirect` creates an `HttpResponseRedirect` object, which is a specialized HTTP response with a status code of `302` (Found) by default.
        - This `302` status code tells the browser to issue a new GET request to the specified URL. It is temporary `redirect`.

    - Create a function to redirect to a newly build function if the admin is valid.

  - [ ] Why can't we use Render? Because the URL does not change.

  - [x] Task to do : Use the internal CSS in a different CSS file and link it using Block in the `user.html`.

# **Week 2 (2081-04-24 to 04-32)**

### **04-24**

- **Tasks**

  - [x] Explain about Admin Page. All the components

    - [x] Add URL for the `admin-page`. Then redirect using `redirect` function.

    - [x] Link images and css

    - [x] Configure `logout`

      - Add url, function

        - `{% url 'logout' %}`

        ```python
         def Logout(request):
           log_user = request.user.id
           print(log_user)
           logout(request)
           return redirect('login')
        ```

        - On logging out, the session is cleared. Open the inspect window -> Applications to show.

  - [x] Render the Registration Page

    - Initially, explain HTML of the registration page.

  - [x] Include block element in the body and link.

    - [x] Add Block for the Links

      ```python
        {% extends 'auth/admin.html' %}
        {% load static %}
        {% block links %}
        <link rel="stylesheet" href="{% static 'admin/user_reg.css' %}" />
        {% endblock %}
      ```

    - [x] Add Block for the Body

      - Add Body block in admin.html

    - [x] Do not add tags for Teachers

    - In Django Template Language (DTL), the {% block %} tag is a powerful feature used for template inheritance. It allows you to define sections (blocks) of a template that can be overridden by child templates. This enables a consistent layout across multiple pages while allowing each page to customize specific sections.

    - {% block block_name %} {% endblock %}
    - {% block block_name %} {% endblock %}

    - It creates a hole that is to be filled by the template that will inherit it.

  - [x] Extend the `admin.html` to `user.html`

    - [x] Extend tag. Template Inheritance. `extends .html`

      - Template inheritance in Django is a powerful feature that allows you to create a base or parent template that defines a common structure for your website and then extend or customize this structure in child templates. This approach promotes the reuse of HTML code and helps in maintaining consistency across multiple pages of a website.

    - Reusability. As we make change in one place and it will be reflected in the other as well.

  - [x] Create different CSS file for the CSS. Make it external and link using blocks.

- [x] Handle Form Submission

  - Use CSRF Token

  ```python
      def UserRegistration(request):
        print(request.POST)
        if request.method == "POST":
          fn = request.POST.get("first_name")
          ln = request.POST.get("last_name")
          un = request.POST.get("username")
          em = request.POST.get("email")
          print(em)
          pw1 = request.POST.get("pswd1")
          pw2 = request.POST.get("pswd2")
          if pw1 == pw2:
            if User.objects.filter(username=un).exists():
              messages.info(request,f"The User With {un} already exists")
              print("User Exists")
              return render(request,'auth/registration.html')
            else:
              user = User.objects.create_user(username=un,first_name=fn,last_name=ln,password=pw1,email=em)
              user.save()
              messages.info(request,"User Has Been Sucessfully Registered")
              print("Matches")
          else:
            messages.info(request,"The passwords didn't matched")
            return render(request,'auth/registration.html')
        else:
          pass
        return render(request,'auth/registration.html')
  ```

## **Tasks**

### **04-27**

- [x] Create a User from the form data

- [x] This method of creating User is not relevant to Industry. As we've not used any Validation. But before that.

- [x] Till now I can type whatever URL I want to visit any page. But in real world it should not happen. To prevent that we use `@login_required`. It is provided by Django's Authentication System.

  - [x] Login Required Decorator

    - Import : `from django.contrib.auth.decorators import login_required`

    - Syntax : `login_required(redirect_field_name='next', login_url=None`)

      - Here, If the user isn’t logged in, redirect to `settings.LOGIN_URL`, passing the current absolute path in the query string. Example: `/accounts/login/?next=/polls/3/`

        - Inside settings we define the default path for `LOGIN_URL = '/'`

      - If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.

  - [x] Working of Login Required Decorator

    - Checks if the user is authenticated. If the user is authenticated, the view function is executed else, they are redirected to the login page.

    - If we enter any random URL we can see `http://127.0.0.1:8000/?next=/admin-page/` this type of URL. Here, there's next=/admin-page/ which tells us that where should it be redirected after we login.

    - We will get `302` status code as response i.e. redirect. Go to the inspect to show.

    - We can also give default redirect URL in the `settings` `LOGIN_REDIRECT_URL = '/profile/'`

  - [x] How does decorator works?

    - As we know functions are made to perform a single task. If we start adding conditions and extra logic beside core task of the function which affects it's reusability.

    - Decorators allows us to separate the additional concerns from the core logic.

    - We must know, we can pass function as parameter and one function can return another function object.

    - [x] What is a decorator?

      - It is a function which takes a function, modifies the function and returns the function. It is a design pattern that allows us to modify the functionality of a function by passing it in another function.

      - The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.

      - **Simple Decorator**

      - We are modifying the function to run after 2 seconds delay.

      ```python
        import time

        def timer_decorator(func):
            def wrapper():
                start_time = time.time()
                result = func()
                end_time = time.time()
                print(f"Execution time: {end_time - start_time} seconds")
                return result
            return wrapper

        def my_function():
            time.sleep(2)
            print("Function executed")

        a = timer_decorator(my_function)
        a()
      ```

  - Now, here we've been using variable to store the function call but Python provides a much elegant way to achieve this functionality using the `@` symbol.

    ```python
      import time

      def timer_decorator(func):
          def wrapper():
              start_time = time.time()
              result = func()
              end_time = time.time()
              print(f"Execution time: {end_time - start_time} seconds")
              return result
          return wrapper

      @timer_decorator
      def my_function():
          time.sleep(2)
          print("Function executed")

      my_function()
    ```

  - **Note** : If we use `@` the function that needs to be decorated should be called. Like as shown above.

  - **Another Example**

    - Let's create a function to check if we can divide the numbers.

    - Here, we are checking if the values are divisible in another function i.e. another function extends the functionality of another function.

    ```python
    def smart_divide(func):
      def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
        print("Oops! cannot divide")
        return

        return func(a, b)
      return inner

    @smart_divide
    def divide(a, b):
    print(a/b)

    divide(2,5)
    ```

    - The above is similar to

    ```python
      def smart_divide(func):
        def inner(a, b):
            print("I am going to divide", a, "and", b)
            if b == 0:
                print("Oops! cannot divide")
            else:
                func(a, b)
        return inner

      def divide(a, b):
      print(a/b)

      a = smart_divide(divide)
      a(2, 0)
    ```

  - [x] Function similar to login_required

  ```python

  def login_required(func, next):
      def wrapper(request):
          if request.user.is_authenticated:
            func(request)
          else:
              return redirect('login-page')
      return wrapper

  def admin_view(request):
      return "HTML"

  request = "blah"
  next = "/admin-page"

  result = login_required(admin_view)
  print(result(request, next))

  ```

- [x] Day Task : Create User Registration form using Django Forms.

  ```python
    from django import forms

    class UserRegistrationForm(forms.Form):
      first_name = forms.CharField(
      max_length=100,
      widget=forms.TextInput(attrs={'placeholder': 'Enter your first name', 'required': 'required'}),
      label="First Name"
      )
      last_name = forms.CharField(
      max_length=100,
      widget=forms.TextInput(attrs={'placeholder': 'Enter your last name', 'required': 'required'}),
      label="Last Name"
      )
      username = forms.CharField(
      max_length=100,
      widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'required': 'required'}),
      label="Username"
      )
      email = forms.EmailField(
      widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'required': 'required'}),
      label="Email"
      )
      password1 = forms.CharField(
      widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'required': 'required'}),
      label="Password"
      )
      password2 = forms.CharField(
      widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password', 'required': 'required'}),
      label="Confirm Password"
      )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
  ```

  - [x] Use custom validation for each field.

    ```python
      def clean_first_name(self):
          first_name = self.cleaned_data.get('first_name')
          if not first_name.isalpha():
              raise ValidationError("First name should contain only alphabetic characters.")
          return first_name

      def clean_last_name(self):
          last_name = self.cleaned_data.get('last_name')
          if not last_name.isalpha():
              raise ValidationError("Last name should contain only alphabetic characters.")
          return last_name

      def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        return username
    ```

  - [x] Without RegEx.

    - Suppose we want to check if the Password contains a Number or Not

      ```python
        numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        password = 'admin'

        for i in password:
            if i in numbers:
                print("Password is strong")
                break
        else:
            print("Password is weak")
      ```

    - But we've a better way if we use RegEx. Library used for pattern matching in String.

  - [x] With RegEx

    ```python
      import re
      pswd = 'admin1'
      result = re.search('[0-9]', pswd)
      print(result)
    ```

## **Tasks**

### **04-32**

- [x] Explain `login_required` again

  - Explain how `next` works in the `login_required` decorator.
  - Create a Request object with GET parameter that has the GET requested URL. Or an attribute that stores the current URL to explain `login_required` decorator.

- [x] Problem with `login_required` `next` parameter.

  - Previously when we try to enter custom URL, after we logged in we were redirected to the `admin-page-name`. Instead we should have been redirected to `next` URL. To solve this

  - Suppose, we're trying `http://127.0.0.1:8000/register/` initially. It will send request to `path('register/', views.register_user, name='register'),`.

  - Since, we've used decorator for this view. The function `(register_user)` is passed as a call back (in this case it is not called) to the decorator so that it can be called later if the user is authenticated else the decorator calls `login_page` view.

  - The request object is passed in the `inner_function` of the `login_required` decorator.

    - Let's consider a scenario when the user is not authenticated. Here, the decorator first checks if the `request.user.is_authenticated` in our case it will be false. Then, it will capture the `/register/` from the `request` object and return `HttpResponseRedirect` object of for `login` view path via `LOGIN_URL`.

    - As, we know when we've `HttpResponseRedirect` we get `location` attribute in the response header and our location attribute would look like `location: /?next=/register/`. As soon as the browser gets `302` i.e. `Redirect Status Code` status code it will create a new URL with the `location` attribute which would look like `http://127.0.0.1:8000/?next=/register/` and send `HttpGetRequest` to `http://127.0.0.1:8000/` along with `/?next=/register/` as `Query Parameter`.

    - Here is the catch, why are we using `/?` in the URL? Because it has a special meaning. We are not sending request to a single URL `http://127.0.0.1:8000/?next=/register/` instead we are sending request to `http://127.0.0.1:8000/` along with `Query String`.

      - **Query Parameter/String**

        - The `?` in a URL indicates the beginning of a Query String.

        - It is used to pass additional parameters or data to a web server.

        - One thing to `Note` is that `Query String` are always stored in the `GET` attribute of the `Request` object. No matter what type of request we are sending if we've Query String the URL they are always stored in the `GET` attribute.

    - So, here we are sending request to `http://127.0.0.1:8000/` along with `?next=/register/` as `Query String`. The `Query String` is passed in the GET Request body. Everything after `?` in the URL is passed as `Query String` in the form of key-value pair.

    - For Example, let's submit a `GET` request for a form submission of the `Login Page`. We can see all the information in the URL with a `Query String`. `http://127.0.0.1:8000/?csrfmiddlewaretoken=auQy6KxUHsqKksaIHcRmaf9omnW9E73mSF3KklZZns2T9qzCsEMD9CNDmeC5S9o3&username=admin&password=admin`.

  - Then, once the user submits the login form. A `POST` Request along with `Query Parameters` we capture the `next` and then `redirect`

  - As we're `redirected` to `login` we've to modify the `login_page` view.

  - Capture the next parameter in the URL. Then `redirect` to `next` if `next` is not `None` else `admin-page-name`

  ```python

    next = request.GET.get('next')
    print(f"Next: {next}")

    return redirect(next if next else 'admin-page-name')

  ```

- [x] Inspect the window to see the PayLoad

- [x] Send some random data by using Query String in the URL

- [x] Example of `login_required` decorator with next parameter.

```python

  class User:
      def __init__(self,uname,is_authenticated):
          self.username = uname
          self.is_authenticated = is_authenticated

  class Request:
      def __init__(self,post,method,user,url,get=None):
          self.GET = get
          self.POST = post
          self.method = method
          self.user = user
          self.url = url

  class HttpResponseRedirect:
      def __init__(self,redirect_url):
          self.location = redirect_url
          self.status_code = 302

  def redirect(to):
      print(f'Redirecting to http://127.0.0.1:8000{to}')
      return HttpResponseRedirect(to)

  user_object = User('admin', False)
  request_url = '/register/'
  req_object = Request({}, 'GET', user_object, request_url)

  def login_required(func):
      def inner(request):
          if request.user.is_authenticated:
              func(request)
          else:
              prepare_redirect_url = f'/?next={request.url}'
              return redirect(prepare_redirect_url)
      return inner

  @login_required
  def register_user(request):
      print("Register User")

  print(register_user(req_object).location)
  print(register_user(req_object).status_code)

```

- [x] After This

  - Request is sent by the browser to the `login` page with `/?next=/register/` as Query String.

  ```python

  class User:
      def __init__(self,uname,is_authenticated):
          self.username = uname
          self.is_authenticated = is_authenticated

  class Request:
      def __init__(self,post,method,user,url,get=None):
          self.GET = get
          self.POST = post
          self.method = method
          self.user = user
          self.url = url

  class HttpResponseRedirect:
      def __init__(self,redirect_url):
          self.location = redirect_url
          self.status_code = 302

  def browser(to):
      print("Opening Browser")
      print(f"Sending request to http://127.0.0.1:8000/{to}")
      login_page(req_object)

  def redirect(to,flag=None):
      print(f'Redirecting to http://127.0.0.1:8000{to}')
      # return HttpResponseRedirect(to)
      if not flag:
          browser(to)
      else:
          print(req_object.user.is_authenticated)

  user_object = User('admin', False)
  request_url = '/register/'
  req_object = Request({},'POST',user_object,request_url,get={'next' : request_url})

  def login_required(func):
      def inner(request):
          if request.user.is_authenticated:
              func(request)
          else:
              prepare_redirect_url = f'/?next={request.url}'
              redirect(prepare_redirect_url)
      return inner

  @login_required
  def register_user(request):
      print("Register User")

  def login_page(request):
      if request.method == 'GET':
          print("Sending Login Page")
          print("\n")
      else:
          print("Printing GET data")
          print("\n")
          print(request.GET.get('next'))
          print("\n")
          print("We are getting form data")
          print("Validating form data")
          print("Login the User")
          print("Redirecting to Next Parameter")
          print("\n")
          request.user.is_authenticated = True
          redirect(request.GET.get('next'),1)

  register_user(req_object)

  ```

- [x] Problem Multiple Validation for Password1

  - When we use multiple validation, if an error is raised for a field then other fields are not checked. The error will be raised for the field which do not pass the validation.

- [x] Password Validation

  - We do not need to check the clean_password2 because if one is not valid that's enough. Plus we've already performed validation for Password1. Therefore, Password2 is only to match with the first.

  - Check if two passwords are the same or not.

  ```python

    def clean(self):
      cleaned_data = super().clean() // Returns cleaned_data
      password1 = cleaned_data.get("password1")
      password2 = cleaned_data.get("password2")

      if password1 and password2 and password1 != password2:
          raise forms.ValidationError("Passwords do not match.")

      return cleaned_data
  ```

- [x] More information regarding RegEx. Here, we've used basic RegEx as per our need but in real world we've to use complex RegEx for strict validation.

- [x] Take individual Data from the `cleaned_data` attribute.

- [x] Create a User.

  ```python
  user = User.objects.create_user(
                  username=username,
                  email=email,
                  password=password1,
                  first_name=first_name,
                  last_name=last_name
              )
  ```

- [x] Display the errors in the frontend.

- [x] Send Message to the Frontend (Notification)

  - To display message, create HTML which only displays when we've message.

  - First Display HTML without DTL tag.

    - Here, we only have to display message when we've message else we've to hide the HTML.

  - Then apply CSS in the `user_reg.css`

  - We are inside the body part of the Inherited Admin Page. So we need to include Script and Style Tag inside the body. Therefore, we've to use `{% end if %}` after style tag.

  ```Python
    {% if messages %}
      {% for message in messages %}
          <div class="toast" id="toast{{ forloop.counter }}">
            <div class="toast-content">
                <i class="fas fa-solid fa-check check"></i>
                <div class="message">
                    <!-- <span class="text text-1">Success!</span> -->
                    <span class="text text-2">{{message}}</span>
                </div>
            </div>
            <!-- <i class="fa-solid fa-xmark close"></i> -->
            <i class="fas fa-times close" id="close{{ forloop.counter }}"></i>
            <div class="progress"></div>
        </div>
    {%endfor%}
  ```

  - We add `{% endif %}` below the `<script></script>` tag.

- [x] CSS for the Toast

  - We add the below CSS in the `reg.css` file.

  - The `{% if messages %}` should have it's end after the script because we want to use the script only if there's message.

  ```CSS
  .toast{
      position: absolute;
      top: 25px;
      border-radius: 12px;
      background: #fff;
      padding: 20px 35px 20px 25px;
      box-shadow: 0 5px 10px rgba(0,0,0,0.1);
      border-left: 6px solid #4070f4;
      overflow: hidden;
      transform: translateX(calc(100% + 30px));
      transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.35);
  }
  .toast.active{
      transform: translateX(0%);
  }
  .toast .toast-content{
      display: flex;
      align-items: center;
  }
  .toast {
              transition: opacity 0.5s, height 0.5s, margin 0.5s, padding 0.5s;
          }
  .toast-content .check{
      display: flex;
      align-items: center;
      justify-content: center;
      height: 35px;
      width: 35px;
      background-color: #4070f4;
      color: #fff;
      font-size: 20px;
      border-radius: 50%;
  }
  .toast-content .message{
      display: flex;
      flex-direction: column;
      margin: 0 20px;
  }
  .message .text{
      font-size: 20px;
      font-weight: 400;;
      color: #666666;
  }
  .message .text.text-1{
      font-weight: 600;
      color: #333;
  }
  .toast .close{
      position: absolute;
      top: 10px;
      right: 15px;
      padding: 5px;
      cursor: pointer;
      opacity: 0.7;
  }
  .toast .close:hover{
      opacity: 1;
  }
  .toast .progress{
      position: absolute;
      bottom: 0;
      left: 0;
      height: 3px;
      width: 100%;
      background: #ddd;
  }
  .toast .progress:before{
      content: '';
      position: absolute;
      bottom: 0;
      right: 0;
      height: 100%;
      width: 100%;
      background-color: #4070f4;
  }
  .progress.active:before{
      animation: progress 5s linear forwards;
  }
  @keyframes progress {
      100%{
          right: 100%;
      }
  }
  ```

- [x] Explain the JavaScript Code.

  ```
    {% for message in messages %}
    var toast{{ forloop.counter }} = document.getElementById('toast{{ forloop.counter }}');
    var close{{ forloop.counter }} = document.getElementById('close{{ forloop.counter }}');

    close{{ forloop.counter }}.addEventListener('click', function() {
        removeToast(toast{{ forloop.counter }});
    });

    setTimeout(function() {
        removeToast(toast{{ forloop.counter }});
    }, 3000);

    {% endfor %}

    function removeToast(el) {
      el.style.opacity = '0';
      el.style.height = '0';
      el.style.margin = '0';
      el.style.padding = '0';
      setTimeout(function() {
          el.remove();
      }, 500); // delay should match the transition duration
    }

  ```

- [x] Clear Cache and Session form the Browser.

- [x] Display Error Message with Proper CSS

  ```CSS

    /* Error Styling */
    .errorlist {
        list-style: none;
        padding: 0;
        margin: 0;
        margin-top: 5px;
    }

    .errorlist li {
        font-size: 14px;
        color: #d9534f;
        margin-top: 5px;
        padding: 8px 12px;
        background-color: rgba(217, 83, 79, 0.1);
        border: 1px solid rgba(217, 83, 79, 0.4);
        border-radius: 5px;
        position: relative;
        animation: slideIn 0.4s ease-in-out, fadeIn 0.8s ease-in-out;
    }

    /* Animation for Error Messages */
    @keyframes slideIn {
        0% {
            transform: translateY(-10px);
            opacity: 0;
        }

        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }

        100% {
            opacity: 1;
        }
    }

    /* Icon before error message */
    .errorlist li::before {
        content: '⚠️';
        margin-right: 8px;
        font-size: 16px;
        vertical-align: middle;
    }

  ```

## **Tasks**

### **05-02**

- [x] Any user can login with valid credential. But only admin can access the admin page.

- [x] Give access only to admin page.

  - After login

  ```python
  if user.is_superuser:
      return redirect('admin-page-name')
  # return redirect(next if next else 'admin-page-name')
  print("The user is not superuser")

  ```

- [x] Working of authentication with other users

  - `is_superuser` field of the `Auth_User`

- [x] Explain the Purpose of PersonRegistration

  - Why did we create Users using `User` model? We could have just create

  - We are creating users first so that we can utilize the Django's Authentication System.

  - If we just create a normal Model to store user's credential we'll have to write everything from scratch.

  - But if we use Django's Authentication System, the password are encrypted. It provides Authentication System `authenticate` function.

- [x] Person Registration HTML + CSS

  - Explain the features in the Person page. Do not use the Image field for now.

  - Explain the HTML Code. Show Page only with HTML

  - Explain about all the tags

    - We will not work with Images today.

  - Explain about options in the `select` tag.

    - Explain about `value` attribute in the `option` tag.

  - Remove the `Option` tag

  - Extend the `admin` page to include the PersonRegistration

  - Load the {% load static %}

  - Block links in the Person HTML.

  - Include the CSS in the `user_reg.css`

  - Block Body in the Person

  ```CSS
    .input-box select.custom-class {
      height: 45px;
      width: 100%;
      outline: none;
      font-size: 16px;
      border-radius: 5px;
      padding-left: 15px;
      border: 1px solid #ccc;
      border-bottom-width: 2px;
      transition: all 0.3s ease;
    }

    .input-box select.custom-class:focus,
    .input-box select.custom-class:valid {
    border-color: #9b59b6;
    }

    .input-box .custom-file-upload {
    padding: 10px;
    cursor: pointer;
    text-align: center;
    margin-top: 20px;
    background: linear-gradient(135deg, #71b7e6, #9b59b6);
    color: white;
    border-radius: 5px;
    text-align: center;
    }

    .img{
    margin-top: 20px;
    }
  ```

- [x] Set the URL for the Person page.

## **Tasks**

### **05-03**

- [x] Login Required Decorator for Teacher

- [x] Change the Function name to Teacher

- [x] Fetch the Users from the Backend. Fetch all the data except `admin`.

  ```Python

    user_list = User.objects.all()
    User.objects.exclude(is_superuser=True)

  ```

- [x] `objects` attribute

  - It is a manager that allows you to perform database operations like querying, inserting, updating, and deleting records.

- [x] all()

  - When we use `all` Django converts `SELECT * FROM auth_user;`. The equivalent code runs on the DB to fetch the data. The fetched data is stored as QuerySet Objects.

  - Print the `QuerySet`. Explain `QuerySet`.

- [x] Run the Query in the SQLite Browser

  - `SELECT * FROM auth_user;`
  - `SELECT * FROM auth_user WHERE is_superuser != TRUE;`

- [x] Model Manager

  - A model manager is an object that provides an interface to interact with a particular model in Django. It allows you to query the database, create new objects, and perform other operations on the model.

- [x] How Does Objects work and ORM? Takes Longer Time

  - It uses API. As DB and Django are different application so transfer data among themselves they use API. It ORM API which converts `SELECT * FROM auth_user;` which convert it into SQL Query `SELECT * FROM auth_user;`.

  - Therefore, in the background actually a SQL Query is running. The result from the SQL query is then converted into Python Objects of the User Model.

  - As User is a class. So the result from the SQL Query is converted back in to the User Objects and stored in the QuerySet.

  - As we're interacting with a different application apart from Django. It is resource intensive. Suppose, if we've 1000 of rows to fetch then it takes a longer time as it is `I/O` bound task. During I/O bound task our processor does not work rather the Secondary Memory works and Processor waits for the data to be loaded. Therefore, for such heavy task multithreading is used.

- [x] Display the `Users` in the option tag.

  ```python

    {% for person in teacher %}
    <option value="{{person.id}}">{{person.username}}</option>
    {% endfor %}

  ```

- [x] Handling the Form (POST) using Normal HTMl form

  - Do not use Image field for Today's class.

  - Remove `enctype="multipart/form-data"`

- [x] Reason for using `value="{{person.id}}`

  - To identify the which user has been selected. So that we can build relationship later on.

- [x] Handel the Form (POST) using Django Form

- [x] Django Form for the Form

  - Use different convention

```python
class TeacherForm(forms.Form):
    teacher = forms.ModelChoiceField(queryset=User.objects.exclude(is_superuser=True),widget=forms.Select(attrs={'class' : 'custom-class'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))
    primary_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your number','maxlength': '10','minlength': '10'}))
    secondary_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your number','maxlength': '10','minlength': '10'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sex = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],widget=forms.Select(attrs={'class': 'custom-class'}))
```

- [x] ModelChoiceField

  - It used when we need to create a DropDown where the selections include values from the Django Model.

- `queryset = User.objects.all()` : Defines the option available in the dropdown. It is rendered as `<option>` tag.

- [x] Print the form Object

- [x] Use it in the frontend

- [x] Image Field

  - We will ask for the teacher image.

  - Include it in the Frontend.

  - Try without `style="display:none;"` once.

  ```HTML

    <div class="input-box">
      <div class="img">
        <label for="id_my_image" class="custom-file-upload">Upload Image</label>
        <input type="file" id="id_my_image" name="my_image" class="img" style="display:none;" />
      </div>
    </div>

  ```

- [x] Submit the form only as `POST` request.

  - We are only getting the name of the image that is submitted. Because it is not encoded. It is encoded but the encoding used was the encoding that is used to encode text input which means the encoding does not work. Therefore, we need to have separate encoding for `files`.

- [x] Submit the form without `enctype`

  - First, we need to know the data we submit is encoded by the browser.

  - Encoding is done to transmit data across the network properly. Because not all characters or data types can be sent in an HTTP request.

    - As per HTTP protocol, the data that is to be sent over web should be in a specific format. Encoding ensures that the data meet those standards.

    - Our form data contains special characters like `'&',',','=','?'`. These characters have specific meanings in URLs and HTTP request. Encoding prevents these characters from being misinterpreted.

  - When we submit a file without `enctype` data is not sent properly in the server because the encoding used for transferring text input is different from encoding used for files.

- [x] Inspect to show the text encoded

  - Address field of the form

- [x] Solving the encoding problem

  - Open the inspect window to show type of encoding used for the form data in the `content-type` of `Request Header`.

  - As files and image consists of binary data, which cannot be directly sent in plain text. Therefore, we need to use different encoding for the files.

  - We use `enctype="multipart/form-data"`

    - When use multipart, the form data is sent in multiple parts.

    - Non-file fields are sent as simple key-value paris which are encoding by text encoding `application/x-www-form-urlencoded` algorithm is used. It is the default encoding.

    - File fields are sent as binary data along with metadata like `filename`, `content-type` and more. `multipart/form-data` it splits the data in the multiple parts.

  - Since, the data is submitted in the multiple part we can access the text input in the `request.POST` attribute and file data in the `request.FILES`.

- [x] Get the encoded file.

  - Print the FILE object
  - Meta data related to files are also present
  - Print the content_type

- [x] Open the inspector window to see the submitted data.

  - Payload -> View Source

  - The form data is divided into different section.

  - When this data arrives at the server, the server fetches the text data as key value-pair and stores in the `POST` attribute and file data into `FILES`. But before it just used to accept key-value as it is.

- [x] Django Form with File Field

  ```python
    my_image = forms.ImageField(
    widget=forms.ClearableFileInput(attrs={
    'class': 'img',
    'style': 'display:none;',
    }), # This sets the label for the field in Django forms
    )
  ```

- [x] Form Validation

  - Pass the text input and file data in the Form Class.

  ```python

  if request.method == 'POST':
    form = TeacherForm(request.POST, request.FILES)
    if form.is_valid():
        print(form.cleaned_data)

  ```

- [x] File Validation

  - `is_valid` will not work. Install the `pillow` library.

  - We cannot let user to upload any files they want. We need to validate the type of file.

  - Validate the size.

  - Valid Content Type

  ```python
  def clean_my_image(self):
    image = self.cleaned_data.get('my_image')
    if image.size > 2*1024*1024: # 2 MB
        raise forms.ValidationError('Image size should not exceed 2MB')

    valid_content_types = ['image/jpeg', 'image/png']

    if image.content_type not in valid_content_types:
        raise forms.ValidationError("Unsupported file type. Please upload a JPEG or PNG image.")

    return image
  ```

  - Submit a video. A PDF greater than 2 MB.

- [x] Create a PDF of the Note.

- [x] Today's Task.

  - Write Validations for the other fields

## **Tasks**

### **05-04**

- [x] Explain the Use of Multithreading for the Tasks that involves Querying

  - As we're interacting with a different application apart from Django. It is resource intensive. Suppose, if we've 1000 of rows to fetch then it takes a longer time as it is `I/O` bound task. During I/O bound task our processor does not work rather the Secondary Memory works and Processor waits for the data to be loaded. Therefore, for such heavy task multithreading is used.

- [x] Teacher Model

  - Display the PDF

  - When we create a model Primary Key is the Id. The same primary key becomes a foreign key while creating a relationship.

  - `OneToOneRelationship` with Teacher

  - Only one User can be a Teacher

  - We will get the First Name, Last Name and Email from the User model. Therefore, we do not need to create extra fields.

  - `MinLengthValidator` : `from django.core.validators import MinLengthValidator`

  - `__str__`

    - String Representation of an Object. It is called only when the Object is printed.

- [x] Class Meta

  - Also, known as Inner Class in Python Class.

  - Allows to specify metadata for a Django Mode, Such as DB table names.

- [x] Attributes in the `class Meta`

  - `db_table` : Name of the DB table. By default the name of the Table will be `appName_className`.

  - `ordering` : Ordering the Query Results. Use `[fieldName]` for Ascending and `[-fieldName]` for Descending.

  - `verbose_name` : Human readable names for the model. These names are displayed in the Django Admin. If not given, underscore will be converted into space.

  - `constraints` : Rules that are applied at the database level to maintain data integrity and consistency. UniqueConstraints keeps the field Unique throughout the record(row).

  - It checks only for the pair of fields to be unique across the table.

  ```python

  class Meta:
    constraints = [
      models.UniqueConstraints(fields=['primary_number','secondary_number'], name='unique_number')
  ]

  ```

- [x] Teacher Model without Image

  ```python
  Gender = [
      ('M','Male'),
      ('F','Female')
  ]

  class Teacher(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      address = models.CharField(max_length=30)
      DOB = models.DateField()
      primary_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=False)
      secondary_number = models.CharField(max_length=10,validators=[MinLengthValidator(10)], null=True)
      sex = models.CharField(max_length=10, choices=Gender)

      def __str__(self):
          return self.user.username

      class Meta:
          db_table = "teacher"
          ordering = ['user']
          verbose_name = "Teacher"
          verbose_name_plural = "Teachers"
          constraints = [
              models.UniqueConstraint(fields=['primary_number','secondary_number'], name='primary_number_check')
          ]

  ```

- [x] Makemigrations and Migrate

  - When we create relationship, `Pk` of one table becomes the `Fk` for the related table.

  - The `Fk` field is displayed as `field_id` in the Table.

- [x] Display the Admin Page without Use of ModelAdmin

- [x] ModelAdmin

  - Go the admin page. Explain `admin.py`
  - It is where we register our models to make them available in the Django Admin Interface. It gives us `CRUD` features.
  - By default only the `User` and `Permission` table is available on the Admin Page.
  - We use `ModelAdmin` classes to customize how models are displayed in the Admin Page.

- [x] Register the Teacher Model

  ```python

  from django.contrib import admin
  from .models import Teacher

  @admin.register(Teacher)
  class TeacherAdmin(admin.ModelAdmin):
      list_display = ['user','address','dob','primary_number','secondary_number','sex']

  ```

- [x] Fix `makemigrations` and `migrate` Issue

  - Delete the `db_sqlite3`.

  - Delete 'migration0001`related files from the`migrations` folder.

- [x] Create Teacher from the Post Request

  ```python

    user = form.cleaned_data['teacher']
    address = form.cleaned_data['address']
    dob = form.cleaned_data['dob']
    primary_number = form.cleaned_data['primary_number']
    secondary_number = form.cleaned_data['secondary_number']
    sex = form.cleaned_data['sex']
    my_image = form.cleaned_data['my_image']

    Teacher.objects.create(user=user,
                            address=address,
                            dob=dob,
                            primary_number=primary_number,
                            secondary_number=secondary_number,
                            sex = sex)

  ```

  - Here, when we are passing `User:Object` in the `user` field of the `Teacher` model. In this case, Django will automatically take the ID of the User Object to create a relationship.

- [x] Display the Admin Page after ModelAdmin usage

- [x] Explain a bit about `Pillow` Library

  - It provides tools to manipulate images, like resizing, cropping, rotating etc.
  - Convert images from one format to another.

  ```python
    from PIL import Image

    # Open an image file
    image = Image.open('example.jpg')

    # Display the image
    image.show()
  ```

- [x] Handling Image (How are Image stored in the DB?)

  - [x] There are multiple ways to store images in the server.

    - Storing images as Binary Data (BLOB - Binary Large Object)

      - The binary of the image is stored directly in the DataBase like MySQL, PostgreSQL. SQLite also supports the BLOB data type but we will not use it. It is resource expensive.

    - Storing Image Paths or URLs in the DataBase and the Image Files on the File System.

      - We will be using this. This process is popular while working in the Development phase.
      - We will make use of Media Files in this process.

    - Storing Images on a Cloud Storage Service ad Storing the URL in the Database

      - Images are stored in the remote cloud storage services like Amazon S3, Google Cloud Storage.

      - The URL of the stored image is then saved in the database.

- [x] The Myth : Images are stored in the DataBase

  - Images are not stored in the DataBase because they are resourceful. If we store binary of the images it will make the DataBase slow. Therefore, URL of the image is stored in the Database.

- [x] Media Files

  - [x] What are Media Files?

    - User uploaded files such as Images, Videos, Documents or any other file are called Media Files.

- [x] Working of Media Files

  - We save the URL for the Image in the DataBase then Django will serve it to the frontend.

- [x] Setting up Media Files Configuration

  - As we know only the URL is stored in the DataBase. Image data should be stored somewhere in the system.

  - We will create a `media` folder in the `BASE_DIR` level.

  - Setting the `MEDIA_ROOT` and `MEDIA_URL`

  ```python

  # settings.py
  MEDIA_ROOT = BASE_DIR / 'media/'
  MEDIA_URL = '/media/'

  ```

- [x] Add the `media` folder in the `.gitignore` file.

  - We will upload heavy data to the Repository.

- [x] What is MEDIA_ROOT and MEDIA_URL? Explain in detail

  - [x] MEDIA_ROOT

    - It gives the root path for the image to be stored.

    - When we use `upload_to` it will provide the path for the image to be saved.

  - [x] MEDIA_URL

    - It provides a URL prefix for all the media files.

    - It defines the URL to access the media files.

    - For example :

- [x] Add ImageField in the Teacher Model

  ```python

    profile_picture = models.ImageField(upload_to='',null=True, blank=True)

  ```

  - Images will be stored in the `media/profile_pics/img.png`

  - It will store the URL of that picture. Here, the URL will be `media/profile_pics/img.png`

- [x] Working of `upload_to`

  - It defines where to save the actual Image data in the File System.

- [x] Create a Teacher 

- [x] Display the Image From `teacher_list.html`

## **Before Further Explanation Use Dummy Image Tag to Show That This Configuration Does Not Work Even If the Path is Correct for the Image**

  - Create an Image Tag to Give the URL for the Image.

  ```python

    <img src="{{ profile.profile_picture.url }}" alt="Profile Picture">

  ```

  - Use Proper Height and Width for the Person. Create a New HTMl file only to show this.

  - Pass the `Teacher Objects` in the Context. Access the URL.

  - Open the SQlite DB to View the URL for the Image.

  - Explain How `.url` works in `profile_picture.url`. What does it render?

    - If we use `.url` it gives the full path with `MEDIA_URL`. 
    - If we do not use it gives the relative path

  - Why do we have to use `.url`?

## **Explain the Reason for Not Working with the Above Configuration.**

- [x] **Doing Only This Will Not Work. We Will Need To Understand How Django Serves Files?**

- [x] **First, How does a request for an Image work? How the static Images are Requested?**

  - We need to understand that everything is request and response in the web. Nothing works without Request and Response.

  - [x] Open the Inspector Window to Explain How Request for Images are Sent?

  - [x] What is the Difference between requesting for a Static Image and Media Image.
    - One thing to note is that we didn't map the `static` URL because Django by default maps the Static Files to the Static Folder. 
    - But in case of Media Files we have to explicitly serve the Media Files.

  - [x] How Images are Requested and Served?

    - Open the Inspector window to Explain how request are sent to retrieve images.

## Final Configuration for the Media Files to Work 

- [x] Now, We Add the Path for the Media Files
  - In the Main AMS `urls.py`

  ```python

  from django.conf.urls.static import static
  from django.conf import settings


  if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  ```

- [x] URL Pattern after Adding the Path for Media Files

  - `static` function takes two arguments `prefix` and `document_root`.

  - `prefix` should be match with `settings.MEDIA_URL`

  - `document_root` is the directory where the files are stored. As files are stored in the `settings.MEDIA_ROOT`

  - It will return a single Path that will map the given `prefix` to the view that serves the files from the given directory.

  - Here, `serve` is the `view` which takes two arguments i.e. `path` and `MEDIA_ROOT`. It is the main function that is serving the Media Files.

    ```

    urlpatterns = [

        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

    ```

- [x] Reason Behind the Use of `static` method to map MEDIA_URL to MEDIA_ROOT

  - The initial Request URL will look like this `http://127.0.0.1:8000/media/pic1.png`.

    - Here, actually the Base URL i.e. `http://127.0.0.1:8000` is mapped to `/D/AMS_CV_Deerwalk/ams/urls/`. So our MEDIA_URL will look like `/D/AMS_CV_Deerwalk/ams/urls/media/pic1.png`. Therefore, we cannot directly map to the File System or the Root Media Folder.

  - But our actual path for the Media File is `/D/AMS_CV_Deerwalk/media/pic1.png`.

  - To know that a `request` is being made for a Media File we use `MEDIA_URL`

  - Therefore, we need to map it to the actual URL.

## Serving in Development Vs Production

- [x] How does Django server Media Files? In Development Vs Production

- [x] Give an Example to Explain the Work Flow

- [x] Accessing the Image in the Frontend

  ```python

  <img src="{{ profile.profile_picture.url }}" alt="Profile Picture">
  <a href="{{ profile.resume.url }}">Download Resume</a>

  ```

## **Task**

### **05-09**

- [x] First Store the Photos of two teachers.

  - Now a problem arises with this implementation, what if the name of the photos are same?
  
  - For Example : A submitted `pic.png` and B submitted `pic.png` in this case the later one will override the image. Therefore, we need to handle it correctly.

  - [x] Handling the Overriding Problem

    ```python

    def user_directory_path(self, filename):
        # File will be uploaded to MEDIA_ROOT/user_<id>_<filename>
        return f'user_{self.user.id}_{filename}'

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        profile_picture = models.ImageField(upload_to=user_directory_path)

    ```

    - `self` is the currently running object. Filename will be the name of the file.

    - If we use `f'user_{instance.user.id}/{filename}'` then it will be stored in the `MEDIA*ROOT/user*<id>/<filename>`

- [ ] Create `Teacher` with already used `User`

  - Create a Teacher with a User that has been already used to create Teacher.

- [ ] Handling Errors Raised Due to DataBase Validations.

  - [ ] Handling Unique Constraints Failed in Real World Project

  ```python

    user = form.cleaned_data['teacher']
    address = form.cleaned_data['address']
    dob = form.cleaned_data['dob']
    primary_number = form.cleaned_data['primary_number']
    secondary_number = form.cleaned_data['secondary_number']
    sex = form.cleaned_data['sex']
    my_image = form.cleaned_data['my_image']

    if Teacher.objects.filter(user=user).exists():
      form.add_error('teacher', f'Teacher with {user.username} already exists')

    else:
        try:
            Teacher.objects.create(user=user,
                            address=address,
                            dob=dob,
                            primary_number=primary_number,
                            secondary_number=secondary_number,
                            sex = sex)
        except Exception as e:
            print(e)
            form.add_error(None, 'Teacher with this number already exists')

  ```

  - We can add our custom error in the form using `add_error` the first parameter should be `form Field Name`.

- [ ] Notification for the Teacher Creation

  - [ ] Send Message for Successful Teacher Assignment


## **Task**

### **05-11**

- [x] Fix Notification Not Working 

```Js
close{{ forloop.counter }}.addEventListener('click', function () {
```
  - Remove the space to fix

- [x] Redirect to the `admin` page or `add_student` view

- [x] Configure CSS for Student Page

- [x] Validation for the Option tag. User can change the {{person.id}}. How to handel such modification?

- [x] Configure Add Student Page

- [x] Explain Add Student Feature

- [x] Student Model 

  ```python
  from django.db import models
  from django.core.validators import MinLengthValidator

  GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ]

  class Student(models.Model):
      name = models.CharField(max_length=100)
      address = models.CharField(max_length=250)
      age = models.PositiveIntegerField(
          validators=[
              MinValueValidator(1),
              MaxValueValidator(99)
          ]
      )
      phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)],unique=True)
      
      gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
      class Meta:
          verbose_name = "Student"
          verbose_name_plural = "Students"
          ordering = ['name']

      def __str__(self):
          return self.name
  ```
  - We can also use RegEx validators

- [x] Django Form for the Student 

  ```python

  from django import forms

  class StudentForm(forms.Form):
      # Name field
      name = forms.CharField(
          max_length=100,
          required=True,
          widget=forms.TextInput(attrs={'placeholder': 'Enter Student Name', 'class': 'input-box'})
      )

      # Address field
      address = forms.CharField(
          max_length=250,
          required=True,
          widget=forms.TextInput(attrs={'placeholder': 'Enter Student Address', 'class': 'input-box'})
      )

      # Age field with integer validation and range constraint
      age = forms.IntegerField(
          required=True,
          min_value=1,
          max_value=99,
          widget=forms.NumberInput(attrs={'placeholder': 'Enter Student Age', 'maxlength': '2', 'minlength': '1', 'class': 'input-box'})
      )

      # Phone number field with exactly 10 digits validation using RegexValidator
      phone_number = forms.CharField(
          required=True,
          widget=forms.TextInput(attrs={'placeholder': 'Enter Student Phone Number', 'maxlength': '10', 'minlength': '10', 'class': 'input-box'})
      )

      # Gender field (commented out in your HTML but included for completeness)
      GENDER_CHOICES = [
          ('M', 'Male'),
          ('F', 'Female'),
          ('O', 'Other'),
      ]
      gender = forms.ChoiceField(
          choices=GENDER_CHOICES,
          required=True,
          widget=forms.Select(attrs={'class': 'custom-class', 'id': 'id_sex'})
      )
  ```
- [x] Validation for the Fields

```python

  def clean_name(self):
      name = self.cleaned_data.get('name')
      if not re.match(r'^[a-zA-Z\s]+$', name):
          raise forms.ValidationError("Name must contain only letters and spaces.")
      return name

  # Custom validation for the 'address' field
  def clean_address(self):
      address = self.cleaned_data.get('address')
      if len(address) < 10 or len(address) > 250:
          raise forms.ValidationError("Address must be between 10 and 250 characters.")
      return address

  # Custom validation for the 'age' field
  def clean_age(self):
      age = self.cleaned_data.get('age')
      if age < 1 or age > 99:
          raise forms.ValidationError("Age must be between 1 and 99.")
      return age

  # Custom validation for the 'phone_number' field
  def clean_phone_number(self):
      phone_number = self.cleaned_data.get('phone_number')
      if not re.match(r'^\d{10}$', phone_number):
          raise forms.ValidationError("Phone number must be exactly 10 digits.")
      return phone_number

  # Custom validation for the 'gender' field (optional)
  def clean_gender(self):
      gender = self.cleaned_data.get('gender')
      if gender not in dict(self.GENDER_CHOICES).keys():
          raise ValidationError("Invalid gender selected.")
          return gender

```

- [x] It is optional to the same validations in the Model as we've already used it in the Backend

- [x] Handle POST Request

- [x] Create Student Objects

  ```python
    from .forms import StudentForm

    def create_student(request):
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                return redirect('some_success_url')
        else:
            form = StudentForm()
        return render(request, 'create_student.html', {'form': form})
  ```

- [x] Introduction to Model Form

  - Model forms in Django are a powerful feature that automatically create a form from a Django model.

  - They provide an easy way to handle forms, including rendering, validation, and saving data to the database, based on model fields.

- [x] How to Create Model Form

  - Created using the `ModelForm` class. 

  -  When you use a model form, it automatically generates form fields and validation rules based on the fields defined in the corresponding model.


  ```python

  from django import forms
  from .models import Student

  class StudentForm(forms.ModelForm):
      class Meta:
          model = Student
          fields = ['name', 'address', 'age', 'phone_number', 'gender']
  ```

- [x] Write Form Field Validations in the Form Class

  ```python

  from django import forms
  from .models import Student
  import re
  from django.core.exceptions import ValidationError

  class StudentForm(forms.ModelForm):
      class Meta:
          model = Student
          fields = ['name', 'address', 'age', 'phone_number', 'gender']

      # Custom validation for the 'name' field
      def clean_name(self):
          name = self.cleaned_data.get('name')
          if not re.match(r'^[a-zA-Z\s]+$', name):
              raise forms.ValidationError("Name must contain only letters and spaces.")
          return name

      # Custom validation for the 'address' field
      def clean_address(self):
          address = self.cleaned_data.get('address')
          if len(address) < 10 or len(address) > 250:
              raise ValidationError("Address must be between 10 and 250 characters.")
          return address

      # Custom validation for the 'age' field
      def clean_age(self):
          age = self.cleaned_data.get('age')
          if age < 1 or age > 99:
              raise ValidationError("Age must be between 1 and 99.")
          return age

      # Custom validation for the 'phone_number' field
      def clean_phone_number(self):
          phone_number = self.cleaned_data.get('phone_number')
          if not re.match(r'^\d{10}$', phone_number):
              raise ValidationError("Phone number must be exactly 10 digits.")
          return phone_number

      # Custom validation for the 'gender' field (optional)
      def clean_gender(self):
          gender = self.cleaned_data.get('gender')
          if gender not in ['M', 'F', 'O']:
              raise ValidationError("Invalid gender selected.")
          return gender
  ```

- [x] Create Student Object Using Model Form

  ```python
    def create_student(request):
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                # Save the validated form data to the database
                form.save()
                return redirect('success_page')
        else:
            form = StudentForm()
        return render(request, 'create_student.html', {'form': form})
  ```

  - When we use form.save() it creates instance of the Model

- [x] Notification
- [x] Redirect
- [x] Explain the URL for Media Files

## **Task**

### **05-11**

## **Article Idea**

- [x] Tampering the HTML form

  ```python
    Yes, the above solution works if the User with the modified User ID is already created in the Teacher Table. But what if the User with the modified ID is not created as Teacher Object? In this case we will choose different User in the Frontend but actually are creating Teacher with different User. For Example below will be my Select tag that will be rendered by Django Form 

    <select name="teacher" class="custom-class" required="" id="id_teacher">
      <option value="">---------</option>

      <option value="2" selected="">Birat</option>

      <option value="3">Umesh</option>

      <option value="4">Suman</option>

    </select>

    But what if I changed the `<option value="4">Suman</option>` to `<option value="2">Suman</option>`. Also, not that Teacher for User ID 2 is not created in this case we are choosing different User and creating data for different User. How such scenario are handled in the real world? Explain in detail. 
  ```

- [x] The problem with creating Teacher with Invalid ID. Inspect window to change the ID for new user. 

  - When the form is submitted, new Teacher will not be created as we've used `ModelChoiceField` due to which it will try to create an `Teacher Object` but if we do not have a `User` with that ID it won't be able to create a `Teacher Object`. Therefore, the form will not be valid. An error is added to that field. 
  
  - But what if we pass the Valid ID for the `value` attribute of the `select` tag. Here, also we will have two cases. 
    - First, If the user with the Valid ID is already created then the form will be valid but as we move forward to create Teacher object. As we've `OneToOne Field` for the `Teacher` the `exists()` method will check due to the `Teacher` will not be created for that ID. 
    - Second, what if the object of the `Teacher` with the modified ID of `User` is not created? In this case the `Teacher` object will be created but the Information of that particular `User` will be stored in the DataBase. Here, the problem is that we've selected a different `User` and data will be stored for another `User`. 

- [x] How can we Fix it?

  - **Solution Not Found Yet**
  - **Solution Idea**

    - Here, I've noted one thing. In such type of scenario the ID gets duplicated among the fetched User. So we can stored the initial IDs of the Fetched User then later check if there is duplication. But I don't we can identify duplication because we will be receiving only one value. 

    - Use different value for the `value` attribute. Here we are using the ID. 
  
    - **We need to some how manage to submit final value of the `value` attribute of the `Select Option` tag so that we can check duplication. **
    
      - This works for that we will need to Use JavaScript to capture the final values of the `value` attribute and submit it in the hidden field as different key in the `POST` request. Below is the code.
      
      ```html

        <form method="POST" enctype="multipart/form-data" onsubmit="captureValues()">
            {% csrf_token %}
            {{ form.as_p }}
            
            <!-- Hidden field to store all valid user IDs -->
            <input type="hidden" name="all_user_ids" id="all_user_ids" value="">

            <button type="submit">Submit</button>
        </form>

        <script>
            function captureValues() {
                var selectElement = document.getElementById("id_teacher");
                var options = selectElement.options;
                var allValues = [];

                for (var i = 0; i < options.length; i++) {
                    allValues.push(options[i].value);
                }

                // Join all the values into a single string separated by commas
                document.getElementById("all_user_ids").value = allValues.join(',');
            }
        </script>
      ```


      ```python

      @login_required
      def teacher(request):
          user_list = User.objects.exclude(is_superuser=True)
          form = TeacherForm()

          if request.method == 'POST':
              # Get the submitted list of all user IDs
              all_user_ids = request.POST.get('all_user_ids').split(',')

              # Get the user ID selected in the form submission
              selected_user_id = request.POST.get('teacher')

              # Check if the selected user ID is in the list of all user IDs
              if selected_user_id not in all_user_ids:
                  form.add_error('teacher', 'Invalid user selection. Please try again.')
                  return render(request, 'auth/PersonRegistration.html', {'teachers': user_list, 'form': form})

              # Get the User object based on the selected ID
              try:
                  user = User.objects.get(id=selected_user_id)
              except User.DoesNotExist:
                  form.add_error('teacher', 'Selected user does not exist.')
                  return render(request, 'auth/PersonRegistration.html', {'teachers': user_list, 'form': form})

              # Create the form instance with the request data
              form = TeacherForm(request.POST, request.FILES)

              if form.is_valid():
                  # Now check for the existing Teacher object
                  if Teacher.objects.filter(user=user).exists():
                      form.add_error('teacher', f'User with {user.username} already exists')
                  else:
                      try:
                          Teacher.objects.create(user=user,
                                                address=form.cleaned_data['address'], 
                                                dob=form.cleaned_data['dob'], 
                                                primary_number=form.cleaned_data['primary_number'], 
                                                secondary_number=form.cleaned_data['secondary_number'],
                                                sex=form.cleaned_data['sex'],
                                                image=form.cleaned_data['my_image'])
                          messages.success(request, 'Teacher Created Successfully')
                      except Exception as e:
                          form.add_error(None, 'Error in Creating User')
              else:
                  print("Form is Invalid")
                  print(form.errors)

          return render(request, 'auth/PersonRegistration.html', {'teachers': user_list, 'form': form})
      ```

  - [x] But what if the ID equals the ID of `admin` we also have to handle for such scenario. 

### Today's Content

- [x] Explain Add Course HTML

- [x] Link the CSS and HTML with Admin Page

  - Remove CSS
  - Remove the Notification

- [x] Link Add Course in the Admin

  - `<li><a href="{% url 'add-course' %}">`

- [x] Create a View for the Add Course

- [x] Pass teacher as Context. Display Teachers to Choose

  ```python

    def add_course(request):
        teachers = Teacher.objects.all()
        print(request.POST)
        return render(request, 'auth/addcourse.html', {'teachers': teachers})
  ```

  ```HTML
    <select name="teacher" id="teacher" class="custom-class" required>
      {% for item in teachers %}
      <option value="{{item.id}}">{{item.user.first_name}} {{item.user.last_name}}</option>
      {% endfor %}
    </select>
  ```

  - Here, we're using `user` field to access the other information as we've a Relationship with the `User` model. But this is not the optimal way. 

- [x] Use of `all()` and `prefetched_related`

  - Running query is expensive. I've also told while teaching why can't we use Binary for the Image in DB. 

  ```python

    teachers = Teacher.objects.all()
    teachers = Teacher.objects.prefetch_related('user').all()

```

  - [x] `all()`

    - It is used only when we have to use fields from only one model. It fetches without any optimization in the DataBase. If we use `all` to retrieve related fields then we will have performance issue. Though we can retrieve we should not use it if we want fields from the related field. 

    - It's equivalent SQL Query is `SELECT * FROM teacher;`

    - The problem here is that if we try to fetch the related fields then it will make an additional query to the DataBase due to which it affects performance. If we use `item.user.first_name`

    ```SQL
     SELECT first_name FROM auth_user WHERE id = 2;
    ```

  - [x] `prefetch_related('user').all()`

    - It is used to retrieve all records from the `teacher` model and efficiently preload related objects of the Relationship Model. It performs a separate query to fetch related objects and then caches them. 
    - It performs separate query to fetch the related fields and caches them for future use. It is efficient than `all()` as it prevents `n+1` query. 

    ```SQL
      SELECT * FROM auth_user WHERE id IN (
      SELECT user_id FROM teacher
      );
    ```
    - It will only use two query to fetch all the data. 

- [x] Display the Teachers in the Add Course Page.

- [x] Display Teachers in the Admin Page. 

  - [x] Images 

  ```html

  {% for teacher in teachers %}

    <div class="card">
      <!-- Replace with actual image URL -->

      <img src="{{teacher.image.url}}" alt="Teacher Image">

      <!-- Replace with teacher's first and last name -->
      <h4>{{ teacher.user.first_name }} {{ teacher.user.last_name }}</h4>
      <h5>Address</h5><span>{{ teacher.address }}</span>
      <h5>DOB</h5><span>{{ teacher.dob }}</span>
    </div>
  {% endfor %}

  ```
    - [x] Working of Via Media Files

    - [x] Adding the path for the Media File
      - Explain the Request Response Cycle for Media Files

  - [x] Teacher Details

- [x] Handel Post Request

  - Print all the data

- [x] Django Form for Add Course

```python

class CourseForm(forms.Form):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), widget=forms.Select(attrs={'class' : 'custom-class'}))
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Course Title'}),
        required=True,
        label='Title'
    )

    duration = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Course Duration'}),
        required=True,
        label='Duration'
    )

    shift = forms.ChoiceField(
        choices=[('M', 'Morning'), ('D', 'Day')],
        widget=forms.Select(attrs={'class': 'custom-class'}),
        required=True,
        label='Shift'
    )

    # Custom validation for title field
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    # Custom validation for duration field
    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if not duration.isdigit():
            raise forms.ValidationError("Duration should be a number.")
        return duration

```

## **05-18**
### **Today's Content**

- [x] Field Validation

  ```python

  # Custom validation for duration field
  def clean_duration(self):
      duration = self.cleaned_data.get('duration')
      if not duration.isdigit():
          raise forms.ValidationError("Duration should be a number.")
      return duration

  ```

- [x] Create Model for the Course

  ```python

  class Course(models.Model):
    title = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    shift = models.CharField(max_length=1, choices=shift_choice)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
      
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ["title"]

  ```

  - [x] `ForeignKey` Explain

    - [x] Why can't we use `ForeignKey` in the `Teacher` model? Why do we have to use it in the `Course` Model only? 

    - [x] We are creating `OneToManyField`. One `Teacher` can have many relationship with `Course`. 

  - [x] Early planning Unique fields for Model Form

- [x] Register the Model in Admin Page

- [x] Save the data with Django Form

- [x] Model Form for the Course 

```python

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'duration', 'shift', 'teacher']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title', 'class': 'custom-class'}),
            'duration': forms.TextInput(attrs={'placeholder': 'Enter Duration', 'class': 'custom-class'}),
            'shift': forms.Select(attrs={'class': 'custom-class'}),
            'teacher': forms.Select(attrs={'class': 'custom-class'}),
        }
    
    # Custom validation for duration (ensuring it's numeric and valid)
    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if not duration.isdigit():
            raise forms.ValidationError("Duration must be a number.")
        if int(duration) <= 0:
            raise forms.ValidationError("Duration must be a positive number.")
        return duration

```

- [x] View for Model Form 

- [x] Add the choice field to the Form

```python 

def add_course(request):
    teachers = Teacher.objects.prefetch_related('user').all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        print("Form")
        print(form)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
        else:
            # Print form errors in case of invalid data
            print(form.errors)
    else:
        form = CourseForm()
        form.fields['teacher'].choices = [(teacher.id, f'{teacher.user.first_name} {teacher.user.last_name}') for teacher in teachers]
        print("Get Request")
        print(form)
    return render(request, 'auth/addcourse.html', {'form': form})

```
 
- [x] Notification

- [x] Add Login Required Decorator

- [x] Explain about the DataBase Structure Till Now

- [x] Add Student Class

  - Till now we've assign Courses to Teacher. But we still do not know which student are enrolled in which course. 

- [x] Explain `addclass.html`

  - We need to select multiple `Student` for a single `Course`. For that we use `multiple` attribute. 

- [x] Display Students and Courses

- [x] Add Link in the `Admin.html`

- [x] Display all the Students in the `admin.html`

- [x] Extend `Admin.html`

- [x] Add the below CSS in the `user_reg.css`

```CSS

/* Add Student Class CSS */

.select2-container--default .select2-selection--multiple {
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
    cursor: pointer;
    display: block;
    height: 45px;
    user-select: none;
    white-space: nowrap;
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
}

.select2-container--default .select2-selection--multiple .select2-selection__choice {
    background-color: #9b59b6;
    border: none;
    border-radius: 4px;
    color: #fff;
    cursor: default;
    float: left;
    margin-right: 5px;
    margin-top: 5px;
    padding: 0 5px;
}

.select2-container--default .select2-selection--multiple .select2-selection__choice__remove {
    color: #fff;
    cursor: pointer;
    display: inline-block;
    font-weight: bold;
    margin-right: 2px;
}

.select2-container--default .select2-selection--multiple .select2-selection__choice__remove:hover {
    color: #fff;
}

```

- [x] Final `addclass.html`

```HTML


{% extends 'auth/admin.html' %}
{% load static %}

{% block links %}
  <link rel="stylesheet" href="{% static 'admin/user_reg.css' %}">
  <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/css/select2.min.css" rel="stylesheet" />
{% endblock %}

{% block body %}

<div class="body">
    <div class="containers">
        <div class="title">Student Class Details</div>
        <div class="content">
      <form  method="POST">
        {% csrf_token %}
        <div class="user-details">
            <div class="input-box">
                <span class="details">Choose Students</span>
                <select name="student" id="teacher" class="custom-class select2-multiple" multiple>
                    {% for student in students %}
                    <option value="{{student.id}}" >{{student.name}}</option>
                    {% endfor %}
                </select>
              </div>
              <div class="input-box">
                <!-- <label for="teacher">Teacher</label> -->
                <span class="details">Choose Course</span>
                <select name="course" id="teacher" class="custom-class" required>
                    {% for course in courses %}
                    <option value="{{course.id}}">{{course.title}}</option>
                    {% endfor %}
                </select>
              </div>
        </div>

        <div class="button">
          <input type="submit" value="Submit">
        </div>

      </form>
        </div>
    </div>

<script>
{% for message in messages %}
    var toast{{ forloop.counter }} = document.getElementById('toast{{ forloop.counter }}');
    var close{{ forloop.counter }} = document.getElementById('close{{ forloop.counter }}');
    
    close{{ forloop.counter }}.addEventListener('click', function() {
        removeToast(toast{{ forloop.counter }});
    });

    setTimeout(function() {
        removeToast(toast{{ forloop.counter }});
    }, 3000);
{% endfor %}

function removeToast(el) {
    el.style.opacity = '0';
    el.style.height = '0';
    el.style.margin = '0';
    el.style.padding = '0';
    setTimeout(function() {
        el.remove();
    }, 500); // delay should match the transition duration
}
</script>
</div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js"></script>
<script>
$(document).ready(function() {
    $('.select2-multiple').select2({
        placeholder: 'Click or Search'  // Change this to your desired placeholder text
    });
});   
</script>

{% endblock %}

```

- [x] Display all Course and Student

- [x] Print the `POST` request

  - We receive all the ids of the selected student

- [x] Create the AddStudentClass Model

```python

class StudentClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title
    
    class  Meta:
        db_table = 'Class'
        verbose_name_plural = 'Classes'
        ordering = ['course']

```
  - We will use `ForeignKey` on both the fields. 

- [x] Register in the Admin Page

- [x] Create Model Instance with This IDs

  - Access all the IDs. 

  - If we use `request.POST['student']` or `request.POST.get('student')` we will get a single value because it is designed to return the first value by default. 

  - Instead we should use `getlist()` i.e request.POST.getlist('student)

  - If we try to save using the below:

  ```python
    students = Student.objects.all()
    courses = Course.objects.all()
    if request.method == 'POST':
        print(request.POST)
        course_id = request.POST.get('course')
        for item in request.POST.getlist('student'):
            StudentClass.objects.create(student=item, course=course_id)
  ```

  - We will get an error because we're trying to assign a string i.e `course_id` and `student_id` as `'1'` to the course field. It expects Course instance. Therefore, it is always better to use Django Forms to handle Form. Django Form will create all the Model Instance based on the provided data `request.POST` to the Django Form. 

  - We will need to create `course_instance = Course.objects.get(id=course_id)` and assign the field to the `course` field. Also, create `student` instance for that ID. Then create the objects. 

- [x] Create AddStudent Instance without Form

```python

def add_student_class(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    if request.method == 'POST':
        print(request.POST)
        course_id = request.POST.get('course')
        course_instance = Course.objects.get(id=course_id)
        for item in request.POST.getlist('student'):
            student_instance = Student.objects.get(id=item)
            StudentClass.objects.create(student=student_instance, course=course_instance)
            print("Student ID", item)
    return render(request, 'auth/addclass.html', {'students': students, 'courses': courses})

```

- [x] Create Django Form for the AddStudent Class with Validation

```python

from django import forms
from .models import StudentClass, Student, Course

class StudentClassForm(forms.Form):
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'custom-class select2-multiple',
            'id': 'students'
        }),
        required=True
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={
            'class': 'custom-class',
            'id': 'course'
        }),
        required=True
    )

    def clean_students(self):
        students = self.cleaned_data.get('students')
        if not students:
            raise forms.ValidationError("Please select at least one student.")
        return students

    def clean_course(self):
        course = self.cleaned_data.get('course')
        if StudentClass.objects.filter(course=course).exists():
            raise forms.ValidationError(f"The course '{course.title}' already has an assigned class.")
        return course
```

- [x] Explain about `ModelMultipleChoice` Field

  - Previously we've used `ModelChoiceField` which let's us choose a single option, but now we've to select multiple options. 
  - We use `SelectMultiple` so that we've `multiple` attribute in our `select` tag. 

- [x] Field Validations

  - Let's validate only course

- [x] View for Django Form 

```python

def add_student_class(request):
    if request.method == 'POST':
        form = StudentClassForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            students = form.cleaned_data['students']
            course = form.cleaned_data['course']

            # Create a StudentClass instance for each student
            for student in students:
                StudentClass.objects.create(course=course, student=student)
            
            messages.success(request, "Class details submitted successfully!")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentClassForm()
    
    return render(request, 'auth/addclass.html', {'form': form})

```

- [x] Add the form fields in the `frontend`

### Do Not Use Model Form

- [x] ModelForm for the AddStudentClass

```python
class StudentClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = ['course', 'student']

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={'class': 'custom-class', 'id': 'course'}),
        required=True
    )

    student = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'custom-class select2-multiple', 'id': 'student'}),
        required=True
    )

```
  - Previously we've only used `widgets` but we will now have to use customize our `FormFields` because our Model by default will not include the `ModelMultipleChoiceField`. 

- [x] Validation for the Model Form

- [x] View to handle the Form 

```python

def add_student_class(request):
    if request.method == 'POST':
        form = StudentClassForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            students = form.cleaned_data['student']

            # Ensure the creation of a StudentClass for each student
            for student in students:
                StudentClass.objects.create(course=course, student=student)
            
            messages.success(request, 'Student classes have been successfully added.')
            return redirect('success_page')  # Replace 'success_page' with your desired redirect
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentClassForm()

    return render(request, 'auth/addcourse.html', {'form': form})

```

- [x] Search How to Deal with ModelForm error

- [x] Notification

- [x] Create a separate app for Teacher Features

- [x] Handle Login for Other User except `Admin`

- [x] Create View for the Teacher Login

- [x] Explain `CourseList.html`

## **05-19**
### **Tasks**

- [ ] Reason for New App

- [ ] Create a new app i.e `attendance`

- [ ] Explain Base HTML

- [ ] Explain Course List HTML page. 

- [ ] Display Course List HTML

- [ ] Extend the base HTML

- [ ] Login for Teacher

```python

if user is not None:
  print("User is authenticated")
  login(request, user)
  if user.is_superuser:
      return redirect('admin-page-name')
  # return redirect(next if next else 'admin-page-name')
  else: 
      print("Not Admin")
      return redirect('course_list')
else:
  print("User is not authenticated")

```

- [ ] `Urls.py` for the new App

- [ ] Create a view to handle course list

- [ ] Display Base HTML

- [ ] Include the Nav HTML in Core

- [ ] Add Blocks in the Base HTML

  - For Links
  - For Title 
  - For Body

- [ ] Link the static files for Base HTML

- [ ] Initial Base HTML 

```HTML

<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Block for additional links (CSS files, etc.) to be added here later -->
  <!-- Block link -->

  <!-- Link to a static CSS file (update with actual static path) -->
  <link rel="stylesheet" href="../static/nav.css">

  <!-- Block for the title to be dynamically filled -->
  <!-- Block Title -->
  <title>Page Title</title>
</head>

<body>
  <!-- Include navigation template file here later -->
  <!-- Include navigation HTML -->

  <!-- Block for the body content to be dynamically filled -->
  <!-- Block body -->

  <nav>
    <div class="left-section">
      <!-- Static image source for the logo -->
      <img src="static/images/deerwalklogo.png" alt="Logo" class="logo-image">
      <!-- Link to the home page (url to be filled in later) -->
      <a href="url_to_home_page" class="course nav-link">Home</a>
      <!-- Link to the profile page (url to be filled in later) -->
      <a href="url_to_profile_page" class="profiles nav-link">Profile</a>
    </div>
    
    <div class="right-section">
      <!-- Link to the logout page (url to be filled in later) -->
      <a href="url_to_logout_page" class="sign-out nav-link">Log Out</a>
    </div>
  </nav>

</body>

</html>

```

- [ ] Load static files for Nav HTML

- [ ] Final Base HTML

```HTML

<!doctype html>
<html lang="en">
{% load static %}
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Block for additional links (CSS files, etc.) to be added here later -->
  <!-- Block link -->

  {% block link %}
  {% endblock %}

  <!-- Link to a static CSS file (update with actual static path) -->
  <link rel="stylesheet" href="{% static 'nav.css' %}">

  <!-- Block for the title to be dynamically filled -->
  <!-- Block Title -->
   {% block title %}
  <title>Page Title</title>
  {% endblock %}
</head>

<body>
  <!-- Include navigation template file here later -->
  <!-- Include navigation HTML -->

  {% include 'core/nav.html' %}

  <!-- Block for the body content to be dynamically filled -->
  <!-- Block body -->
   {% block body %}
   {% endblock body %}

</body>

</html>

```

- [ ] Extend Base HTML in the Course List HTML

- [ ] Link the CSS for the Course List HTML

- [ ] Prefetch Related all Course and Teacher 

  - [ ] We need to Identify Teacher to display the Courses

  - [ ] Prefetch for that User only. 

  - [ ] Access the User using `request.user.id`

  - [ ] Access the Teacher using the User.id

  - [ ] Access all the courses for that Teacher ID

  ```python

  user_id = request.user.id
  teacher = Teacher.objects.get(user = user_id)
  courses = Course.objects.filter(teacher=teacher.id).prefetch_related('teacher')
  print(courses)

  ```

- [ ] Display all the course Card for the Teacher

```HTML

<!-- Extend the base template -->
{% extends 'core/base.html' %}

{% load static %}

{% block link %}
<link rel="stylesheet" href="{% static 'course.css' %}">
{% endblock %}
<!-- End Block -->

<title>Logged In</title>
<!-- End Block -->

<!-- Block for the body content -->
{% block body %}
<div class="center">
  <h1 class="h1">Courses Taught</h1>

  {% for item in courses %}
  <!-- Loop through course details -->
  <div class="blog_post">
    <!-- Uncomment and update image source if needed -->
  
    <div class="container_copy">
      <h3>Course Name </h3>
      <!-- Course title -->
      <h1>{{item.title}}</h1>

      <h3> Teacher </h3>
      <!-- Teacher's first and last name -->
      <h1>{{item.teacher.user.first_name}} {{item.teacher.user.last_name}}</h1>

      <h3>Description </h3>
      <p>This Course is Taught by {{item.teacher.user.first_name}} {{item.teacher.user.last_name}}</p>

      <div class="button2">
        <!-- Link to take attendance (update with actual URL) -->
        <a href="path/to/take-attendance"><button class="calendar">Take Attendance</button></a>

        <!-- Link to download report (update with actual URL) -->
        <a href="path/to/download-report"><button class="cal-report">Report</button></a>
      </div>
    </div>
  </div>
  {% endfor %}
  <!-- End For Loop -->
</div>
<!-- End Body -->
{% endblock %}

```

- [ ] Explain the Profile HTML Page

- [ ] Configure URL Path for Profile in the Nav HTML

- [ ] View for Profile HTML

- [ ] Initial Profile HTML

```HTML

<!DOCTYPE html>
<html lang="en">
  <!-- Load static files -->

  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Profile</title>

    <!-- Custom CSS files -->
    <link rel="stylesheet" href="path/to/static/profile_style.css" />
    <link rel="stylesheet" href="path/to/static/profile_responsive.css" />
    <link rel="stylesheet" href="path/to/static/nav.css" />

    <!-- Remix Font Icons CDN -->
    <link
      href="https://cdn.jsdelivr.net/npm/remixicon@2.2.0/fonts/remixicon.css"
      rel="stylesheet"
    />
  </head>

  <body>
    <!-- Include navigation bar -->

    <div class="body">
      <!-- Body Main-Background -->
      <span class="main_bg"></span>

      <!-- Main-Container -->
      <div class="container">
        <!-- Header/Navbar -->
        <header>
          <div class="brandLogo">
            <figure>
              <img
                src="path/to/static/images/deerwalklogo.png"
                alt="logo"
                width="40px"
                height="40px"
              />
            </figure>
            <span> Deerwalk Institute Of Technology</span>
          </div>
        </header>
        <!-- User Main-Profile -->
        <section class="userProfile card">
          <div class="profile">
            <figure>
              <!-- If no profile image, show default image -->

              <img
                src="path/to/static/images/deerwalklogo.png"
                alt="birat"
                width="250px"
                height="250px"
              />
              <!-- {% else %} -->
              <img
                src="path/to/profile_image_url"
                alt="profile"
                width="250px"
                height="250px"
              />
              <!-- Replace with profile image URL -->

              <!-- Endif -->
            </figure>
            <div class="media-file">
              <form method="POST" enctype="multipart/form-data">
                <!-- CSRF token for form security -->

                <!-- Render form fields as paragraph -->

                <button class="remove">
                  <a href="path/to/image-delete-url">Remove</a>
                  <!-- Replace with URL for image deletion -->
                </button>
                <button class="upload" type="submit">Upload</button>
              </form>
            </div>
          </div>
        </section>
        <!-- Work & Skills Section -->
        <section class="work_skills card">
          <!-- Work Container -->
          <div class="work">
            <h1 class="heading">Work</h1>
            <div class="primary">
              <h1>Deerwalk Institute of Technology</h1>
              <p>
                Sifal <br />
                Kathmandu, Nepal
              </p>
            </div>
            <br /><br />
            <!-- Skills Container -->
            <div class="skills">
              <h1 class="heading">Skills</h1>
              <ul>
                <li style="--i: 0">Android</li>
                <li style="--i: 1">Web-Design</li>
                <li style="--i: 2">UI/UX</li>
                <li style="--i: 3">Video Editing</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- User Details Sections -->
        <section class="userDetails card">
          <div class="userName">
            <h1 class="name">First Last Name</h1>
            <!-- Replace with user's first and last name -->
            <div class="map">
              <i class="ri-map-pin-fill ri"></i>
              <span>Address</span>
              <!-- Replace with user's address -->
            </div>
            <h2>Courses Taught</h2>
            <!-- Loop through courses taught by the user -->

            <p>Course Title</p>
            <!-- Replace with course title -->
            <!-- End for -->
          </div>
          <br />
        </section>

        <!-- Timeline & About Sections -->
        <section class="timeline_about card">
          <div class="tabs">
            <ul>
              <li class="about active">
                <i class="ri-user-3-fill ri"></i>
                <span>About</span>
              </li>
            </ul>
          </div>

          <div class="contact_info">
            <h1 class="heading">Contact Information</h1>
            <ul>
              <li class="phone">
                <h1 class="label">Phone:</h1>
                <span class="info">
                  Primary Number (Primary) <br />
                  Secondary Number (Secondary)
                  <!-- Replace with user's phone numbers -->
                </span>
              </li>

              <li class="address">
                <h1 class="label">Address:</h1>
                <span class="info">Address</span>
                <!-- Replace with user's address -->
              </li>

              <li class="email">
                <h1 class="label">E-mail:</h1>
                <span class="info">Email</span>
                <!-- Replace with user's email -->
              </li>

              <li class="site">
                <h1 class="label">Social Media:</h1>
                <!-- Replace with user's social media links -->
                <a href="#"><i class="ri-facebook-circle-line"></i> &nbsp; </a>
                <a href="#"><i class="ri-twitter-line"></i> &nbsp; </a>
                <a href="#"><i class="ri-github-fill"></i> &nbsp; </a>
                <a href="#"><i class="ri-linkedin-box-fill"></i> &nbsp; </a>
              </li>
            </ul>
          </div>

          <div class="basic_info">
            <h1 class="heading">Basic Information</h1>
            <ul>
              <li class="birthday">
                <h1 class="label">Date Of Birth:</h1>
                <span class="info">DOB</span>
                <!-- Replace with user's date of birth -->
              </li>

              <li class="sex">
                <h1 class="label">Gender:</h1>
                <span class="info">Gender</span>
                <!-- Replace with user's gender -->
              </li>
            </ul>
          </div>
          <div class="edit-profile">
            <a href="path/to/edit-profile-url">
              <button class="button2">
                <i class="ri-pencil-fill"></i>Edit Profile
              </button>
              <!-- Replace with URL for editing profile -->
            </a>
          </div>
        </section>
      </div>
    </div>
  </body>
</html>

```

- [ ] Extend the Base HTML to Profile HTML Page

  - Remove the HTML,Body and other tags

  - Use Base `block` tag to add the links

- [ ] CSS for Profile HTML

- [ ] Pass the `Teacher` and `Course` info through context

  - [ ] Display Teacher Image

  - [ ] Display Courses

  - [ ] Display Personal Infos

- [ ] Handle Image and Add

  - Create Image Form

  ```python

  class ImageForm(forms.Form):
      image = forms.ImageField(label="Choose Pic",label_suffix='',widget=forms.FileInput(attrs={'class': 'image'}))

    def clean_my_image(self):
        img = self.cleaned_data.get('my_image')
        if img.size > 1024*1024:
            raise forms.ValidationError('Image size should be less than 1MB')
        
        valid_content_types = ['image/jpeg', 'image/png']
        if img.content_type not in valid_content_types:
            raise forms.ValidationError('Image should be in jpg or png format')
        
        return img
  ```

- [ ] Handle Image POST Request

```python

def profile(request):
    user_id = request.user.id
    teacher = Teacher.objects.get(user = user_id)
    courses = Course.objects.filter(teacher=teacher.id).prefetch_related('teacher')
    form = ImageForm()
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            teacher.image = img
            teacher.save()
            print(request.FILES)
            print("Post")
        else:
            print("Form is Invalid")
    return render(request, 'attendance/profile.html',{
                      'teacher' : teacher,
                      'courses' : courses,
                      'form' : form
                  })
```

- [ ] Handle Image Delete

  - [ ] Create View for Image Delete

```python

def image_delete(request):
  user_id = request.user.id
  teacher = Teacher.objects.get(user = user_id)
  teacher.image = 'NA'
  teacher.save()
  return redirect('profile')

```

- [ ] Display Default Image if Not Image is Available

```HTML

<figure>
  <!-- If no profile image, show default image -->
  {% if teacher.image == 'NA' %}
  <img src="{% static 'images/deerwalklogo.png' %}" alt="birat" width="250px" height="250px" />
  {% else %}
  <img src="{{teacher.image.url}}" alt="profile" width="250px" height="250px" />
  <!-- Replace with profile image URL -->
  {% endif %}
  <!-- Endif -->
</figure>

```

- [ ] Problem with Image Delete

  - [ ] When we delete the Image we are only overriding the Image URL in our DB with `NA`

  - [ ] But the actual image file are still inside our Media_files folder

- [ ] Solution to Delete the Actual Image

```python
import os
from django.conf import settings
from django.core.files.storage import default_storage

def image_delete(request):
    user_id = request.user.id
    teacher = Teacher.objects.get(user = user_id)
    if teacher.image and teacher.image.name != 'NA':
        image_path = os.path.join(settings.MEDIA_ROOT, teacher.image.name)
        print("Image Name")
        print(teacher.image.name)
        if default_storage.exists(image_path):
            default_storage.delete(image_path)
    teacher.image = 'NA'
    teacher.save()
    return redirect('profile')
```

  - Here, we cannot use `teacher.image.url` because it will get Path with `/media/` i.e. used to handle the Media Files request. Therefore, we use `teacher.image.name` to get the full path of the Image. It will give us the relative path from the `settings.MEDIA_ROOT`. 

  - Here, we are deleting the actual file from our system. For that we need `os` library that let's us work with our Operating System `API`. We need the full path of the Image so that we can delete. 

  - Once, we get the full path we need to check if the given `image_path` exists in our server. For that we use `default_storage` method which is an instance of Django's `Storage` class. We've already used this class but we are unaware about it. Then we use `exists` method to check if the file actually exists. If exists then we use `delete` method to delete the file. 

  - Remember when we used `upload_to` in our model. Yes, `upload_to` uses the instance of `Storage` class to actually store in the MEDIA_ROOT folder. 

- [ ] Final Profile HTML 

```HTML

{% extends 'core/base.html' %}

{% load static %}

<!-- Custom CSS files -->

{% block link %}

<link rel="stylesheet" href="{% static 'profile_style.css' %}" />
<link rel="stylesheet" href="{% static 'profile_responsive.css' %}" />
<link href="https://cdn.jsdelivr.net/npm/remixicon@2.2.0/fonts/remixicon.css" rel="stylesheet" />
{% endblock %}


<!-- Remix Font Icons CDN -->

{% block body %}

<div class="body">
    <!-- Body Main-Background -->
    <span class="main_bg"></span>

    <!-- Main-Container -->
    <div class="container">
        <!-- Header/Navbar -->
        <header>
            <div class="brandLogo">
                <figure>
                    <img src="{% static 'images/deerwalklogo.png' %}" alt="logo" width="40px" height="40px" />
                </figure>
                <span> Deerwalk Institute Of Technology</span>
            </div>
        </header>
        <!-- User Main-Profile -->
        <section class="userProfile card">
            <div class="profile">
                <figure>
                    <!-- If no profile image, show default image -->
                    {% if teacher.image == 'NA' %}
                    <img src="{% static 'images/deerwalklogo.png' %}" alt="birat" width="250px" height="250px" />
                    {% else %}
                    <img src="{{teacher.image.url}}" alt="profile" width="250px" height="250px" />
                    <!-- Replace with profile image URL -->
                    {% endif %}
                    <!-- Endif -->
                </figure>
                <div class="media-file">
                    <form method="POST" enctype="multipart/form-data">
                        {% csrf_token %}
                        <!-- CSRF token for form security -->
                        {{form.as_p}}
                        <button class="remove">
                            <a href="{% url 'image-delete' %}">Remove</a>
                            <!-- Replace with URL for image deletion -->
                        </button>
                        <button class="upload" type="submit">Upload</button>
                    </form>
                </div>
            </div>
        </section>
        <!-- Work & Skills Section -->
        <section class="work_skills card">
            <!-- Work Container -->
            <div class="work">
                <h1 class="heading">Work</h1>
                <div class="primary">
                    <h1>Deerwalk Institute of Technology</h1>
                    <p>
                        Sifal <br />
                        Kathmandu, Nepal
                    </p>
                </div>
                <br /><br />
                <!-- Skills Container -->
                <div class="skills">
                    <h1 class="heading">Skills</h1>
                    <ul>
                        <li style="--i: 0">Android</li>
                        <li style="--i: 1">Web-Design</li>
                        <li style="--i: 2">UI/UX</li>
                        <li style="--i: 3">Video Editing</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- User Details Sections -->
        <section class="userDetails card">
            <div class="userName">
                <h1 class="name">{{teacher.user.first_name}} {{teacher.user.last_name}}</h1>
                <!-- Replace with user's first and last name -->
                <div class="map">
                    <i class="ri-map-pin-fill ri"></i>
                    <span>{{teacher.address}}</span>
                    <!-- Replace with user's address -->
                </div>
                <h2>Courses Taught</h2>
                <!-- Loop through courses taught by the user -->
                {% for course in courses %}
                <p>{{course.title}}</p>
                {% endfor %}
                <!-- End for -->
            </div>
            <br />
        </section>

        <!-- Timeline & About Sections -->
        <section class="timeline_about card">
            <div class="tabs">
                <ul>
                    <li class="about active">
                        <i class="ri-user-3-fill ri"></i>
                        <span>About</span>
                    </li>
                </ul>
            </div>

            <div class="contact_info">
                <h1 class="heading">Contact Information</h1>
                <ul>
                    <li class="phone">
                        <h1 class="label">Phone:</h1>
                        <span class="info">
                            {{teacher.primary_number}} (Primary) <br />
                            {{teacher.secondary_number}} (Secondary)
                            <!-- Replace with user's phone numbers -->
                        </span>
                    </li>

                    <li class="address">
                        <h1 class="label">Address:</h1>
                        <span class="info">{{teacher.address}}</span>
                        <!-- Replace with user's address -->
                    </li>

                    <li class="email">
                        <h1 class="label">E-mail:</h1>
                        <span class="info">{{teacher.user.email}}</span>
                        <!-- Replace with user's email -->
                    </li>

                    <li class="site">
                        <h1 class="label">Social Media:</h1>
                        <!-- Replace with user's social media links -->
                        <a href="#"><i class="ri-facebook-circle-line"></i> &nbsp; </a>
                        <a href="#"><i class="ri-twitter-line"></i> &nbsp; </a>
                        <a href="#"><i class="ri-github-fill"></i> &nbsp; </a>
                        <a href="#"><i class="ri-linkedin-box-fill"></i> &nbsp; </a>
                    </li>
                </ul>
            </div>

            <div class="basic_info">
                <h1 class="heading">Basic Information</h1>
                <ul>
                    <li class="birthday">
                        <h1 class="label">Date Of Birth:</h1>
                        <span class="info">{{teacher.dob}}</span>
                        <!-- Replace with user's date of birth -->
                    </li>

                    <li class="sex">
                        <h1 class="label">Gender:</h1>
                        <span class="info">{{teacher.sex}}</span>
                        <!-- Replace with user's gender -->
                    </li>
                </ul>
            </div>
            <div class="edit-profile">
                <a href="path/to/edit-profile-url">
                    <button class="button2">
                        <i class="ri-pencil-fill"></i>Edit Profile
                    </button>
                    <!-- Replace with URL for editing profile -->
                </a>
            </div>
        </section>
    </div>
</div>

{% endblock %}

```

## **05-25**
### **Tasks**

- [ ] Explain Edit Profile HTML

- [ ] Extend the Base HTML for Edit Profile HTML

- [ ] View for Edit Profile HTML

- [ ] Configure Blocks and Links

- [ ] Use of Disabled attribute in the HTML Tag

- [ ] Using Model Form to Edit the Details Efficiently 

  - In the edit form we've to show the already existing details of the `Teacher`. For that we do not have to pass `Teacher` object through context, instead we can use `ModelForm` to populate the `Form` with existing data then render it in the browser. 

- [ ] Create Model Form for the TeacherEditForm

```python

class TeacherEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['address', 'primary_number', 'secondary_number', 'dob', 'sex']
        widgets = {
            'dob': forms.TextInput(attrs={'disabled': True}),
            'sex': forms.Select(attrs={'disabled': True}),
        }
```

- [ ] Handel the Requests for TeacherEditForm

```python

from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher

def edit_profile(request):
    teacher = Teacher.objects.get(id=2)  # Retrieve the Teacher with ID 2

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            print("Submitted)
            # Redirect to the profile page after saving
        else:
          print("Invalid")
    else:
        form = TeacherForm(instance=teacher)  # Populate the form with the instance data

  return render(request,'attendance/edit-profile.html', {'form': form})

```

- [ ] Problem for `sex` field while using `readonly` attribute. 

  - While we've used `readonly` attribute for `sex` field it will not work as `Users` still can select and submit the form. 

- [ ] Final Solution for TeacherEditForm
  - Use `disable` for both the field. It will not work for `dob` field as `input` with disabled field does not get's submitted with form. But it will not work for `select`. 
  - We will copy the `POST` data and modify it to include the `sex` key with the original value of the `sex`. Similarly, we will use it for `dob`

```python

def edit_profile(request):
    user_id = request.user.id
    teacher = Teacher.objects.get(user = user_id)
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['sex'] = teacher.sex
        post_data['dob'] = teacher.dob

        form = TeacherEditForm(post_data, instance=teacher)

        print(form.data)
        # print(request.POST)
        if form.is_valid():
            form.save()
            print("Submitted")
            # Redirect to the profile page after saving
            return redirect('profile')
        else:
            print("Invalid")
            print(form.errors)
    else:
        form = TeacherEditForm(instance=teacher)  # Populate the form with the instance data

    return render(request,'attendance/edit-profile.html', {'form': form})

```

- [ ] Create a new App for Calender

- [ ] Configure Take Attendance Button

- [ ] Extend the Calender HTML

  - [ ] Blocks and CSS

- [ ] Explain the Calender HTML

- [ ] Create Display Calender View

  - [ ] Explain the Calender UI
  - [ ] JavaScript can be used to display Calender
  - [ ] Explain about `datetime` library

- [ ] Explain `DataTime`

  - [ ] Print the Below Dates

  ```python
    from datetime import date

    todays_date = date.today()
    year = todays_date.year
    day = todays_date.day
    month = todays_date.month

    print("Today's Date")
    print(todays_date)
    print("Year")
    print(year)
    print("Day")
    print(day)
    print("Month")
    print(month)
  ```
  - [ ] We want all the date of the Month. We use `Calender` Library. 

  ```python
    import calendar

    # Calender iterator object for calendar
    cal = calendar.Calendar()
    # Set first day of the week as Sunday
    cal.setfirstweekday(6)

    # Get Month Name
    month_name = calendar.month_name[todays_date.month]
    # Get all the date for the given month. It will return a `generator` object. 
    cal_data = cal.itermonthdays(year,todays_date.month)

    # Print all date
    print("Calender Data")
    print(cal_data)
    for day in cal_data:
        print(day)
  ```
  - [ ] Here 0,0,0 represents that the month does not start from Sunday,Mon,Tuesday
  - [ ] Open the Calender from the Task Bar to show if the dates match
  - [ ] Pass all the dates through context

  ```python

    from datetime import date, timedelta, datetime
    import calendar

    def display_calender(request):
        todays_date = date.today()
        year = todays_date.year
        day = todays_date.day

        print("Today's Date")
        print(todays_date)
        print("Year")
        print(year)
        print("Day")
        print(day)

        # Calender iterator object for calendar
        cal = calendar.Calendar()
        # Set first day of the week as Sunday
        cal.setfirstweekday(6)
        # Month Name 
        month_name = calendar.month_name[todays_date.month]
        # Get all the Days of the Month
        cal_data = cal.itermonthdays(year,todays_date.month)
        print("Calender Data")
        print(cal_data)
        for day in cal_data:
            print(day)
        return render(request, 'attendance/calendar.html',{
            'today':todays_date,
            'month_name':month_name,
            'cal_data':cal_data,
        })

  ```

- [ ] Render the Context Data

  ```HTML

  <!-- Extend the base template -->

  {% extends 'core/base.html' %}

  <!-- Load static files -->

  {% load static %}

  <!-- Block for additional CSS links -->

  {% block link %}

  <link rel="stylesheet" href="{% static 'calendar.css' %}">

  {% endblock %}

  <!-- Block for additional CSS links -->

  {% block title %}

  <title>Calender</title>

  {% endblock %}

  <!-- Block Body -->

  {% block body %}
  <div class="body">
    <br>
    <div class="cal-title">
      <h1 class="body-h1">Monthly Calendar
        <span class="body-span">{{today.year}} {{month_name}} {{today.day}}</span>
        <!-- Replace with dynamic date -->
      </h1>
    </div>
    <div class="calendar">
      <div class="calendar-header">
        <span>{{month_name}}</span> <!-- Replace with dynamic month -->
        <div class="year-picker">
          <span class="year-change" id="prev-year">
            <pre><</pre>
          </span>
          <span id="year">{{today.year}}</span> <!-- Replace with dynamic year -->
          <span class="year-change" id="next-year">
            <pre>></pre>
          </span>
        </div>
      </div>
      <div class="calendar-body">
        <div class="calendar-week-day">
          <div>Sun</div>
          <div>Mon</div>
          <div>Tue</div>
          <div>Wed</div>
          <div>Thu</div>
          <div>Fri</div>
          <div>Sat</div>
        </div>
  ```

- [ ] Iterate over all the Days

  - [ ] We need to note that once a Generator is consumed we cannot use it again. Therefore, we should not use loop in our view to display the Days. Or print the Generator object. 

  - [ ] We use condition to prevent from displaying 0 in the calender

  - [ ] Use Condition to Highlight the Today's date and use link for the Further Attendance Process

  ```HTML
    <div class="calendar-days">
    {% for day in cal_data %}
    {% if day == 0 %}
    <h1 class="h1"></h1>
    {% elif day == today.day %}
    <a href="" class="choose-date">
      <div class="today">
        {{day}}
      </div>
    </a>
    {% else %}
    <div>
      {{day}}
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>
    {% endif %}
    {% endfor %}
    </div>
  ```

- [ ] Explain URL Path Converter

  - [ ] Pass the Course ID 

  ```python

    path('calender/<int:id>', views.display_calender, name='calender'),

    def display_calender(request,id):
        print("ID of the course")
        print(id)
  ```

- [ ] Problem with Passing the Course ID via URL Parameter

  - [ ] User can tamper the URL parameter to avoid this we should use the concept of URL signing

- [ ] Create Choose Date Function

  - [ ] Once the user clicks on Today's Date, render Student_list HTML

- [ ] Create a new Template for Student_List HTML without DTL Tag

```HTML

<!DOCTYPE html>
<html lang="en">

{% load static %}

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
    <!-- DTL: Loading static files for custom styles -->
    <link rel="stylesheet" href="{% static 'student_list.css' %}">
    <title>Student List</title>
</head>

<body>
    <div class="main">
        <h1 class="h1">DWIT Course Attendance
            <!-- DTL: Displaying today's date (day, month, year) dynamically -->
            <span class="h1-span">15 September 2024</span> <!-- Example date -->
        </h1>
        <div class="stu-table">
            <table>
                <thead>
                    <tr>
                        <th class="name-col-1">Student Name</th>
                        <!-- DTL: Loop through attendance report to display dates -->
                        <th class="date-col">12</th> <!-- Example dates -->
                        <th class="date-col">13</th>
                        <th class="missed-col">Status</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- DTL: Start of form tag with POST method and CSRF token -->
                    <form method="POST">
                        <!-- DTL: csrf_token was here -->
                        <tr>
                            <td class="name-col">John Doe</td> <!-- DTL: student.student.name -->
                            <!-- DTL: Loop through attendance report to display attendance statuses -->
                            <td class="status-col">P</td> <!-- Example status -->
                            <td class="status-col">A</td> <!-- Example status -->
                            <td class="attend-col">
                                <div class="input-box">
                                    <!-- DTL: Display dynamic form select options for attendance (Present/Absent) -->
                                    <select name="student1" class="custom-class" required id="id_sex">
                                        <option value="A" selected>Absent</option>
                                        <option value="P">Present</option>
                                    </select>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="name-col">Jane Smith</td> <!-- DTL: student.student.name -->
                            <td class="status-col">P</td> <!-- Example status -->
                            <td class="status-col">P</td> <!-- Example status -->
                            <td class="attend-col">
                                <div class="input-box">
                                    <!-- DTL: Display dynamic form select options for attendance (Present/Absent) -->
                                    <select name="student2" class="custom-class" required id="id_sex">
                                        <option value="A" selected>Absent</option>
                                        <option value="P">Present</option>
                                    </select>
                                </div>
                            </td>
                        </tr>
                        <!-- DTL: End of looping through students and attendance data -->
                    </form>
                </tbody>
            </table>
        </div>
        <div>
            <button type="submit" class="primary">Submit</button>
        </div>
    </div>

    <!-- DTL: Toast messages were dynamically generated here -->
    <div class="toast" id="toast1">
        <div class="toast-content">
            <i class="fas fa-solid fa-check check"></i>
            <div class="message">
                <span class="text text-2">Attendance Submitted Successfully!</span>
            </div>
        </div>
        <i class="fas fa-times close" id="close1"></i>
        <div class="progress"></div>
    </div>

    <style>
        /* Styling for the toast notifications */
        .toast {
            position: absolute;
            top: 90px;
            left: 57%;
            border-radius: 12px;
            background: #fff;
            padding: 20px 35px 20px 25px;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
            border-left: 6px solid #4070f4;
            overflow: hidden;
            transform: translateX(calc(100% + 30px));
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.35);
        }

        .toast.active {
            transform: translateX(0%);
        }

        .toast .toast-content {
            display: flex;
            align-items: center;
        }

        .toast-content .check {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 35px;
            width: 35px;
            background-color: #4070f4;
            color: #fff;
            font-size: 20px;
            border-radius: 50%;
        }

        .toast-content .message {
            display: flex;
            flex-direction: column;
            margin: 0 20px;
        }

        .message .text {
            font-size: 20px;
            font-weight: 400;
            color: #666666;
        }

        .message .text.text-1 {
            font-weight: 600;
            color: #333;
        }

        .toast .close {
            position: absolute;
            top: 10px;
            right: 15px;
            padding: 5px;
            cursor: pointer;
            opacity: 0.7;
        }

        .toast .close:hover {
            opacity: 1;
        }

        .toast .progress {
            position: absolute;
            bottom: 0;
            left: 0;
            height: 3px;
            width: 100%;
            background: #ddd;
        }

        .toast .progress:before {
            content: '';
            position: absolute;
            bottom: 0;
            right: 0;
            height: 100%;
            width: 100%;
            background-color: #4070f4;
        }

        .progress.active:before {
            animation: progress 5s linear forwards;
        }

        @keyframes progress {
            100% {
                right: 100%;
            }
        }
    </style>

    <script>
        /* JavaScript for managing toast notifications */
        var toast1 = document.getElementById('toast1');
        var close1 = document.getElementById('close1');

        close1.addEventListener('click', function () {
            removeToast(toast1);
        });

        setTimeout(function () {
            removeToast(toast1);
        }, 3000);

        function removeToast(el) {
            el.style.opacity = '0';
            el.style.height = '0';
            el.style.margin = '0';
            el.style.padding = '0';
            setTimeout(function () {
                el.remove();
            }, 500); // delay should match the transition duration
        }
    </script>
</body>

</html>

```

- [ ] Clone Master Branch to Work With the Updated HTML

- [ ] Remove the Toast and CSS 

- [ ] Explain Student_list HTML

- [ ] Extend Base HTML 

- [ ] Include all the block Links

- [ ] Create View for the Choose Date

  - [ ] Pass the Today's Date

- [ ] Display the Student_list HTML

  - [ ] Render Today's Date in the Frontend

  - [ ] Pass All the Student's for that Course Using Context 

  ```python

    path('choose-date/<str:passed_date>', views.choose_date, name='choose-date'),

    def choose_date(request,passed_date):
        print("Today's Date")
        print(passed_date)
        todays_date = date.today()
        month_name = calendar.month_name[todays_date.month]
        return render(request, 'calendar/new_student_list.html',{'date':todays_date,'month':month_name})
  ```

- [ ] Passing Date as Path Converter

- [ ] Problem with Date as Path Converter

   - [ ] User can modify the date that is to be saved in the Database

```python
  <a href="{% url 'choose-date' today %}" class="choose-date">

  path('choose-date/<str:date>', views.choose_date, name='choose-date'),

  def choose_date(request,passed_date):
      print("Today's Date")
      print(date)
      return render(request, 'calendar/student_list.html')
```

- [ ] Solution: Access the current date from `datetime` module. 

  ```python

      path('choose-date/<str:passed_date>', views.choose_date, name='choose-date'),

      def choose_date(request,passed_date):
          print("Today's Date")
          print(passed_date)
          todays_date = date.today()
          month_name = calendar.month_name[todays_date.month]
          return render(request, 'calendar/new_student_list.html',{'date':todays_date,'month':month_name})
    ```

- [ ] How to get the Course ID? 

  - [ ] Again pass the Course ID in the Calendar HTML and on the data click pass it again as URL parameter to the Attendance View. 

    - [ ] On doing so we will have to face a problem of URL being temped. Therefore, a better approach would be to create a global variable such that it is changed every time `Take Attendance` button in clicked.

  - [ ] Store the Course ID in the Session for the User

  ```python
    # display_calender view
    request.session['course_id'] = id

    # choose_date view
    course_id = request.session.get('course_id')
  ```

  - [ ] Create Global Variable

    - [ ] Do not use this approach

- [ ] Rewrite the StudentClass Model with proper DB name

  ```python

    def __str__(self):
            return self.student.name

    class Meta:
        db_table = 'student_class'

  ```

- [ ] Makemigration and Migrate the changes

- [ ] Display Student List

  - [ ] Fetch all the student for that Course ID from StudentClass model

- [ ] First We Will Only Work on Taking Attendance for That Course

- [ ] We Will Build the Model Later On 

- [ ] Render all the Students for that course

- [ ] Configure Select Tag as Below in the Student List HTML

```HTML

{% extends "core/base.html" %}
{% load static %}

{% block link %}

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
<link rel="stylesheet" href="{% static 'student_list.css' %}">

{% endblock %}

{% block body %}

<body>
    <div class="main">
        <h1 class="h1">DWIT Course Attendance
            <!-- DTL: Displaying today's date (day, month, year) dynamically -->
            <span class="h1-span">{{date.day}} {{month}} {{date.year}}</span> <!-- Example date -->
        </h1>
        <div class="stu-table">
            <table>
                <thead>
                    <tr>
                        <th class="name-col-1">Student Name</th>
                        <!-- DTL: Loop through attendance report to display dates -->
                        <th class="date-col">12</th> <!-- Example dates -->
                        <th class="date-col">13</th>
                        <th class="missed-col">Status</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- DTL: Start of form tag with POST method and CSRF token -->
                    <form method="POST">
                        {% csrf_token %}
                        <tr>
                            {% for student in students %}
                            <td class="name-col">{{student.student.name}}</td> <!-- DTL: student.student.name -->
                            <!-- DTL: Loop through attendance report to display attendance statuses -->
                            <td class="status-col">P</td> <!-- Example status -->
                            <td class="status-col">A</td> <!-- Example status -->
                            <td class="attend-col">
                                <div class="input-box">
                                    <!-- DTL: Display dynamic form select options for attendance (Present/Absent) -->
                                    <select name="{{student.student.id}}" class="custom-class" required id="id_sex">
                                        <option value="A" selected>Absent</option>
                                        <option value="P">Present</option>
                                    </select>
                                </div>
                            </td>
                        </tr>
                        {% endfor %}

                </tbody>
            </table>
        </div>
        <div>
            <button type="submit" class="primary">Submit</button>
        </div>
        </form>
    </div>
</body>
{% endblock %}

```

- [ ] Print the POST request

- [ ] Get the Each Student Status From the POST Request using the Loop

```python

def choose_date(request,passed_date):
    print("Today's Date")
    print(passed_date)
    course_id = request.session.get('course_id')
    print("Course ID")
    print(course_id)
    print("**********")
    students = StudentClass.objects.prefetch_related('student').filter(course=course_id)
    print(students)
    todays_date = date.today()
    month_name = calendar.month_name[todays_date.month]
    if request.method == "POST":
        print("POST Request")
        print(request.POST)
        print("**********")
        for student in students:
            print(student.student.name)
            print(student.student.id,request.POST.get(str(student.student.id)))
    return render(request, 'calendar/new_student_list.html',{'date':todays_date,'month':month_name,'students':students})

```

- [ ] Create Attendance Model

```python

  status_choice = [
          ('A','Absent'),
          ('P','Present')
      ]

  class Attendance(models.Model):
      today_date = models.DateField(null=True,blank=True)
      student = models.ForeignKey(Student,on_delete=models.CASCADE)
      status = models.CharField(max_length=30,choices=status_choice)
      course = models.ForeignKey(Course,on_delete=models.CASCADE, null=True)

      def __str__(self):
          return (self.student.name)
      
      class Meta:
          db_table = 'Attendance'
          verbose_name_plural = 'Attendance'

```

- [ ] Save the Attendance in the Database for the Student

```python

def choose_date(request):
    course_id = request.session.get('course_id')
    print("Course ID")
    print(course_id)
    print("**********")

    # Today's Date
    todays_date = date.today()
    month_name = calendar.month_name[todays_date.month]

    students = StudentClass.objects.prefetch_related('student').filter(course=course_id)
    print(students)

    if request.method == "POST":
        print("POST Request")
        print(request.POST)
        print("**********")
        for student in students:
            print(student.student.name)
            print(student.student.id,request.POST.get(str(student.student.id)))

            status = request.POST.get(str(student.student.id))
            Attendance.objects.create(today_date=todays_date,student=student.student,status=status,course_id=course_id)
    return render(request, 'calendar/new_student_list.html',{'date':todays_date,'month':month_name,'students':students})

```

### Optional Feature

- [ ] But What Will We Do If the Form Gets Submitted Again for for the Same Date? 

  - [ ] We Should Handle it Using `Clean` method in the our Model

```python

class Attendance(models.Model):
    today_date = models.DateField(null=False,blank=False)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=status_choice)
    course = models.ForeignKey(Course,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.student.name
    
    class Meta:
        db_table = 'Attendance'
    
    def clean(self):
        # Get the number of students enrolled in the course
        enrolled_students_count = StudentClass.objects.filter(course=self.course).count()

        # Count how many attendance records already exist for the specified date and course
        existing_attendance_count = Attendance.objects.filter(today_date=self.today_date, course=self.course).count()

        # Validation rule: the count of existing attendance must not exceed the enrolled students count
        if existing_attendance_count >= enrolled_students_count and not self.pk:  # Check only for new records
            raise ValidationError(f"Cannot create attendance. The number of attendance entries for {self.today_date} exceeds the number of enrolled students.")

    def save(self, *args, **kwargs):
        # Call clean method to perform validation before saving
        self.clean()
        super().save(*args, **kwargs)

```

- [ ] Handling the POST Request after Setting up Constraint

```python

def choose_date(request):
    course_id = request.session.get('course_id')
    print("Course ID")
    print(course_id)
    print("**********")

    # Today's Date
    todays_date = date.today()
    month_name = calendar.month_name[todays_date.month]

    students = StudentClass.objects.prefetch_related('student').filter(course=course_id)
    print(students)

    if request.method == "POST":
        print("POST Request")
        print(request.POST)
        print("**********")
        for student in students:
            print(student.student.name)
            print(student.student.id,request.POST.get(str(student.student.id)))

            status = request.POST.get(str(student.student.id))
            attendance = Attendance(today_date=todays_date,student=student.student,status=status,course_id=course_id)
            try:
                attendance.save()
            except Exception as e:
                print("Error in Saving Attendance")
                print(e)
    return render(request, 'calendar/new_student_list.html',{'date':todays_date,'month':month_name,'students':students})

```

- [ ] Configure Success Message

   - [ ] Paste the Below CSS in the `Student.css`

```CSS

.toast {
  position: absolute;
  top: 90px;
  left: 57%;
  border-radius: 12px;
  background: #fff;
  padding: 20px 35px 20px 25px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  border-left: 6px solid #4070f4;
  overflow: hidden;
  transform: translateX(calc(100% + 30px));
  transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.35);
}

.toast.active {
  transform: translateX(0%);
}

.toast .toast-content {
  display: flex;
  align-items: center;
}

.toast-content .check {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 35px;
  width: 35px;
  background-color: #4070f4;
  color: #fff;
  font-size: 20px;
  border-radius: 50%;
}

.toast-content .message {
  display: flex;
  flex-direction: column;
  margin: 0 20px;
}

.message .text {
  font-size: 20px;
  font-weight: 400;
  color: #666666;
}

.message .text.text-1 {
  font-weight: 600;
  color: #333;
}

.toast .close {
  position: absolute;
  top: 10px;
  right: 15px;
  padding: 5px;
  cursor: pointer;
  opacity: 0.7;
}

.toast .close:hover {
  opacity: 1;
}

.toast .progress {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  width: 100%;
  background: #ddd;
}

.toast .progress:before {
  content: '';
  position: absolute;
  bottom: 0;
  right: 0;
  height: 100%;
  width: 100%;
  background-color: #4070f4;
}

.progress.active:before {
  animation: progress 5s linear forwards;
}

@keyframes progress {
  100% {
      right: 100%;
  }
}

```

- [ ] Final View Without Constraint

```Python

def choose_date(request):
    course_id = request.session.get('course_id')
    print("Course ID")
    print(course_id)
    print("**********")

    # Today's Date
    todays_date = date.today()
    month_name = calendar.month_name[todays_date.month]

    students = StudentClass.objects.prefetch_related('student').filter(course=course_id)
    print(students)

    if request.method == "POST":
        print("POST Request")
        print(request.POST)
        print("**********")
        for student in students:
            print(student.student.name)
            print(student.student.id,request.POST.get(str(student.student.id)))

            status = request.POST.get(str(student.student.id))
            Attendance.objects.create(today_date=todays_date,student=student.student,status=status,course_id=course_id)
        messages.success(request, 'Attendance Marked Successfully')
    return render(request, 'calendar/new_student_list.html',{'date':todays_date,'month':month_name,'students':students})
```

- [ ] Final Student HTML

```HTML

{% extends "core/base.html" %}
{% load static %}

{% block link %}

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
<link rel="stylesheet" href="{% static 'student_list.css' %}">

{% endblock %}

{% block body %}

<div class="main">
    <h1 class="h1">DWIT Course Attendance
        <!-- DTL: Displaying today's date (day, month, year) dynamically -->
        <span class="h1-span">{{date.day}} {{month}} {{date.year}}</span> <!-- Example date -->
    </h1>
    <div class="stu-table">
        <table>
            <thead>
                <tr>
                    <th class="name-col-1">Student Name</th>
                    <!-- DTL: Loop through attendance report to display dates -->
                    <th class="date-col">12</th> <!-- Example dates -->
                    <th class="date-col">13</th>
                    <th class="missed-col">Status</th>
                </tr>
            </thead>
            <tbody>
                <!-- DTL: Start of form tag with POST method and CSRF token -->
                <form method="POST">
                    {% csrf_token %}
                    <tr>
                        {% for student in students %}
                        <td class="name-col">{{student.student.name}}</td> <!-- DTL: student.student.name -->
                        <!-- DTL: Loop through attendance report to display attendance statuses -->
                        <td class="status-col">P</td> <!-- Example status -->
                        <td class="status-col">A</td> <!-- Example status -->
                        <td class="attend-col">
                            <div class="input-box">
                                <!-- DTL: Display dynamic form select options for attendance (Present/Absent) -->
                                <select name="{{student.student.id}}" class="custom-class" required id="id_sex">
                                    <option value="A" selected>Absent</option>
                                    <option value="P">Present</option>
                                </select>
                            </div>
                        </td>
                    </tr>
                    {% endfor %}

            </tbody>
        </table>
    </div>
    <div>
        <button type="submit" class="primary">Submit</button>
    </div>
    </form>
</div>

<!-- DTL: Toast messages were dynamically generated here -->
{% if messages %}
{% for message in messages %}
<div class="toast" id="toast1">
    <div class="toast-content">
        <i class="fas fa-solid fa-check check"></i>
        <div class="message">
            <span class="text text-2">Attendance Submitted Successfully!</span>
        </div>
    </div>
    <i class="fas fa-times close" id="close1"></i>
    <div class="progress"></div>
</div>
{% endfor %}

<script>
    /* JavaScript for managing toast notifications */
    var toast1 = document.getElementById('toast1');
    var close1 = document.getElementById('close1');

    close1.addEventListener('click', function () {
        removeToast(toast1);
    });

    setTimeout(function () {
        removeToast(toast1);
    }, 3000);

    function removeToast(el) {
        el.style.opacity = '0';
        el.style.height = '0';
        el.style.margin = '0';
        el.style.padding = '0';
        setTimeout(function () {
            el.remove();
        }, 500); // delay should match the transition duration
    }
</script>

{% endif %}

{% endblock %}

```

- [ ] Display the 7 Days Status for the Given Student 

- [ ] Store the Past Record of the Students in a Dictionary

```python

def choose_date(request):
    course_id = request.session.get('course_id')
    print("Course ID")
    print(course_id)
    print("**********")

    # Today's Date
    todays_date = date.today()
    month_name = calendar.month_name[todays_date.month]

    students = StudentClass.objects.prefetch_related('student').filter(course=course_id)
    print(students)

    past_dates = [todays_date - timedelta(days=i) for i in range(1,8)]
    print("Past Dates")
    print(past_dates)

    status_dict = {}

    obj = Attendance.objects.get(today_date=todays_date-timedelta(days=2),student=students[0].student,course_id=course_id)
    print("Object")
    print(obj)

    for student in students:
        print(student.student.name)
        status_dict[student.student.id] = {}
        for past_date in past_dates:
            try:
                obj = Attendance.objects.get(today_date=past_date,student=student.student,course_id=course_id)
                status_dict[student.student.id][past_date.day] = obj.status
            except Attendance.DoesNotExist:
                status_dict[student.student.id][past_date.day] = 'NA'
            
    print(status_dict)

```

- [ ] Pass the Past Date and Student Status through Context


```python

def choose_date(request):
  course_id = request.session.get('course_id')
  print("Course ID")
  print(course_id)
  print("**********")

  # Today's Date
  todays_date = date.today()
  month_name = calendar.month_name[todays_date.month]

  students = StudentClass.objects.prefetch_related('student').filter(course=course_id)
  print(students)

  past_dates = [todays_date - timedelta(days=i) for i in range(1,8)]
  print("Past Dates")
  print(past_dates)

  status_dict = {}

  obj = Attendance.objects.get(today_date=todays_date-timedelta(days=2),student=students[0].student,course_id=course_id)
  print("Object")
  print(obj)

  for student in students:
      print(student.student.name)
      status_dict[student.student.id] = {}
      for past_date in past_dates:
          try:
              obj = Attendance.objects.get(today_date=past_date,student=student.student,course_id=course_id)
              status_dict[student.student.id][past_date.day] = obj.status
          except Attendance.DoesNotExist:
              status_dict[student.student.id][past_date.day] = 'NA'
          
  print(status_dict)

  if request.method == "POST":
      print("POST Request")
      print(request.POST)
      print("**********")
      for student in students:
          print(student.student.name)
          print(student.student.id,request.POST.get(str(student.student.id)))

          status = request.POST.get(str(student.student.id))
          Attendance.objects.create(today_date=todays_date-timedelta(days=1),student=student.student,status=status,course_id=course_id)
      messages.success(request, 'Attendance Marked Successfully')
  return render(request, 'calendar/new_student_list.html',{'date':todays_date,'month':month_name,'students':students,'status_dict':status_dict,'past_dates':past_dates})

```

- [ ] Diplay the past 7 days Date 

```HTML
<thead>
  <tr>
      <th class="name-col-1">Student Name</th>
      <!-- DTL: Loop through attendance report to display dates -->
      {% for date in past_dates %}
      <th class="date-col">{{date.day}}</th> <!-- Example dates -->
      {% endfor %}
      <th class="missed-col">Status</th>
  </tr>
</thead>
```

- [ ] How to Access the Status of Past 7 Days from `Status_dict`
  
  - [ ] We can easily access the status for a student using Student ID. For example `{{ status_dict.15.10 }}`
  - [ ] But we've to use `status_dict.student.student.id` to get the same result as above but it will not work because we cannot use `Python` expression in DTL i.e. `status_dict[student.student.id]`

- [ ] Therefore, we Will make Use of Filters to Achieve our Goal. We need to get the Staus of Each Day till the 7th Day. 

  - [ ] We will iterate the Days from our `past_dates`

- [ ] Little bit About Filters in DTL

  - [ ] Filters are used to transform the values of Variables in DTL. 
  - [ ] Filters can be chained
  
- [ ] Example uses of Filter

  - [ ] Use length filter to get the length. Basically filters are built in function, which takes first argument as DTL variable and returns the value to be rendered. 

  ```HTML

  <td class="name-col">{{student.student.name | length}}</td>
  <td class="name-col">{{student.student.name | upper}}

  ```

- [ ] Similary, for Some Advanced Use Cases We can Also make our Custom Filter

 - [ ] To display the status of the past 7 days we will need to build out custom filter. Because to work with nested iterables is hard using DTL.

- [ ] Creating Custom Filter

  - [ ] Create a directory inside the `App` that renders that HTML. `templatetags`
  - [ ] Create a file named `custom_filters.py`
  - [ ] Create the filter function to solve the problem. 
  - [ ] First parameter will be passed as the DTL variable and other parameters are passed as `|filter_name:arg1:arg2`
  - [ ] Syntax for filter : `{{ var_name|filter_name:arg:arg2 }}`

- [ ] We will create two `Filter` one to get the Status Dictioanry of 7 days Using the ID. Another to get the status for individual day. 

- [ ] Complte the `filter`

```python

# custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, id):
    return dictionary.get(id)

@register.filter
def get_status(dictionary, day):
    return dictionary.get(day)

```

- [ ] Load the filter 


```python

{% load custom_filters %}

```

- [ ] Apply the Final Logic

```HTML

{% extends "core/base.html" %}
{% load custom_filters %}
{% load static %}

{% block link %}

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
<link rel="stylesheet" href="{% static 'student_list.css' %}">

{% endblock %}

{% block body %}

<div class="main">
    <h1 class="h1">DWIT Course Attendance
        <!-- DTL: Displaying today's date (day, month, year) dynamically -->
        <span class="h1-span">{{date.day}} {{month}} {{date.year}}</span> <!-- Example date -->
    </h1>
    <div class="stu-table">
        <table>
            <thead>
                <tr>
                    <th class="name-col-1">Student Name</th>
                    <!-- DTL: Loop through attendance report to display dates -->
                    {% for date in past_dates %}
                    <th class="date-col">{{date.day}}</th> <!-- Example dates -->
                    {% endfor %}
                    <th class="missed-col">Status</th>
                </tr>
            </thead>
            <tbody>
                <!-- DTL: Start of form tag with POST method and CSRF token -->
                <form method="POST">
                    {% csrf_token %}
                    {% for student in students %}
                    <tr>
                        <td class="name-col">{{student.student.name}}</td> <!-- DTL: student.student.name -->
                        <!-- DTL: Loop through attendance report to display attendance statuses -->
                        {% for date in past_dates %}
                        <td class="status-col">{{ status_dict|get_item:student.student.id|get_status:date.day }}</td>
                        {% endfor %}
                        <td class=" attend-col">
                            <div class="input-box">
                                <!-- DTL: Display dynamic form select options for attendance (Present/Absent) -->
                                <select name="{{student.student.id}}" class="custom-class" required id="id_sex">
                                    <option value="A" selected>Absent</option>
                                    <option value="P">Present</option>
                                </select>
                            </div>
                        </td>
                    </tr>
                    {% endfor %}
            </tbody>
        </table>
    </div>
    <div>
        <button type="submit" class="primary">Submit</button>
    </div>
    </form>
</div>

<!-- DTL: Toast messages were dynamically generated here -->
{% if messages %}
{% for message in messages %}
<div class="toast" id="toast1">
    <div class="toast-content">
        <i class="fas fa-solid fa-check check"></i>
        <div class="message">
            <span class="text text-2">Attendance Submitted Successfully!</span>
        </div>
    </div>
    <i class="fas fa-times close" id="close1"></i>
    <div class="progress"></div>
</div>
{% endfor %}

<script>
    /* JavaScript for managing toast notifications */
    var toast1 = document.getElementById('toast1');
    var close1 = document.getElementById('close1');

    close1.addEventListener('click', function () {
        removeToast(toast1);
    });

    setTimeout(function () {
        removeToast(toast1);
    }, 3000);

    function removeToast(el) {
        el.style.opacity = '0';
        el.style.height = '0';
        el.style.margin = '0';
        el.style.padding = '0';
        setTimeout(function () {
            el.remove();
        }, 500); // delay should match the transition duration
    }
</script>

{% endif %}

{% endblock %}
```

- [ ] Display the Success Message in Course_List HTML via Message

```python
messages.success(request, 'Attendance Marked Successfully')
return redirect('course-list')
```

- [ ] Add the Message Toast in Course_List HTML

```HTML 
{% if messages %}
{% for message in messages %}
<div class="toast" id="toast1">
    <div class="toast-content">
        <i class="fas fa-solid fa-check check"></i>
        <div class="message">
            <span class="text text-2">Attendance Submitted Successfully!</span>
        </div>
    </div>
    <i class="fas fa-times close" id="close1"></i>
    <div class="progress"></div>
</div>
{% endfor %}

<script>
    /* JavaScript for managing toast notifications */
    var toast1 = document.getElementById('toast1');
    var close1 = document.getElementById('close1');

    close1.addEventListener('click', function () {
        removeToast(toast1);
    });

    setTimeout(function () {
        removeToast(toast1);
    }, 3000);

    function removeToast(el) {
        el.style.opacity = '0';
        el.style.height = '0';
        el.style.margin = '0';
        el.style.padding = '0';
        setTimeout(function () {
            el.remove();
        }, 500); // delay should match the transition duration
    }
</script>

{% endif %}
```

- [ ] Copy the Equivalent CSS for the Above HTML and Past in the Course_List CSS

```CSS
```

### Extra

- [x] Problems with Session

  - Birat : `wjumro78k0es40iz7izphzz7si0p5pyd`

  - Admin : `6ijca6dkcieb9g55jsfc0uak6b1o40qx`

- [x] Add the Image field

- [x] Another way of creating form. ModelForm.

- [x] ModelForm vs Django Form

- [x] URL Path Converter

- Create URL for user-reg

- Use `{% url "name" arg1=v1 arg2=v2 %}` in the hyperlink

- **URL Tag and Path Converter**

- `{% url 'some-url-name' arg1=v1 arg2=v2 %}`
- We can pass argument to the URL as above.
- Give an example to it.

- Create `user_register` view.

- `path('user/<int:id>/ ', views.register_user, name='user_reg')`

  - The above will result in `http://127.0.0.1:8000/user/1/%20` in the given URL We can see `%20` because every character in URL pattern has a special meaning. Therefore, `space` is converted into it's equivalent unicode.
  - URL should not contain space and if there's space it is encoded into it's respective character.

- Passing Context Value in the URL

- `{% url "name" request.user.id %}`
- `{% url "name" name %}`
- We can also pass multiple value

- There can be multiple path converter

- `path('user/<int:id>/<str:name>/', views.register_user, name='user_reg')`
  - We should use `{% url "name" id name %}`

```python
  def register_user(request,id,name):
    print(f"I got an id of {id}")
    return render(request, 'auth/registration.html',{'name' : "Birat"})
```

- If the URL path ({% url "name" name %}) does not find, then we will get `NoReverseMatch` Error.

- [ ] Creating Variables in Template

- As we use alias in Python we can also use it in Template.

- It is useful when we have a long statement.

- For Example : `{% url 'some-url-name' arg as the_url %}`

- Display the variable `<a href="{{ user_reg }}">`

- **Changing the Value in the Select tag for the Student Attendance**


