
from typing import Any, List
import ExpressionClass as ec


class KojoStringValidate:

    def __init__(self,list_container: List,name_check: str = '', name_display: str = '', error_msg: str ='ERROR, Please provide string (A-Z)', number_of_char: int =3) -> None:

        self.name_check = name_check
        self.name_display = name_display
        self.list_container = list_container
        self.number_of_char = number_of_char
        self.error_msg = error_msg


    '''
        This method takes an input and check is it's a string or not.
        If the input is a string it append it to a list.
        If the input is not a string, it informs you to check and make correction.
    '''
    def kojo_validate_string(self) -> str:

        valid = True
        while valid:
            self.name_check = input(f"Enter {self.name_display} ")

            if len(self.name_check) >= self.number_of_char:
                cp = ec.kojo(self.name_check)
                try:
                    if cp == None :
                        print(self.error_msg)
                    else:
                        return self.list_container.append(self.name_check)
                except:
                    pass
            else:
                print(f"You entered {len(self.name_check)} characters minimum character must be {self.number_of_char} character or more")


    def ama_validate_email(self) ->str:
        '''
        This method takes an input and check is it's a string or not.
        If the input is a string it append it to a list.
        If the input is not a string, it informs you to check and make correction.
        '''

        valid = True
        while valid:
            self.name_check = input(f"Enter {self.name_display} ")
            cp = ec.ama(self.name_check)
            try:
                if cp == None:
                    print(self.error_msg)
                else:
                    return self.list_container.append(self.name_check)
            except:
                pass


    def yaw(phone_number:str) ->str:
        pass