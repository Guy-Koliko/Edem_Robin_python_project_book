# PyEdem <br>
<p> This is is a simple module that allows you to do some basic input validation checks</p>
<p>This module is not for big production project but is sutiable for small personal projects where we need to provide validation checks  such as

1. Check if input is a perticular data type
    * String
    * Integer
    * Phonenumber
    * Image
    * Email
2. Format List and Strings
 </p>

 ## <p>HOW TO USE IT </p>
 ```
    """
        To validate user input, just call the BigEclass
        from the BigEclass import KojoStringValidate.
        From KojoStringValidate class you have two methods,
        1. def ama_validate_email(self)
        2. kojo_validate_string(self)
        The methods tells you what you can do with them.

        Note: all the parameter have default values.
        For the email, there is no allowed integer.

        The data entered by a user will be stored into a list that you can use.

    """

 ```
        from BigEclass import KojoStringValidate as BE
        empty_list = []
        name = BE(empty_list,'Name to validate','Text to display to the user','error message to display to the user','an integer, this is the allowed charater the user can enter')
        name.ama_validate_email()

        print(empty_list)

```