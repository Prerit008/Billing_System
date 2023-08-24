# Electricity Billing System [<img src="https://avatars.githubusercontent.com/u/80686842?v=4" width="45" align="right" alt="Prerit Agarwa,">](https://prerit008.github.io/)

This code appears to be a command line program for managing a database of consumers for a utility company.
 <table>
    <tbody>
    <tr>
      <td>
          <a href="https://replit.com/@Prerit008/Electricity-Billing-System" alt="Electricity Billing System" rel="dofollow">
          		<img width="600" src="https://storage.googleapis.com/replit/images/1670911269380_c81efdc6d60a65c5ac481f56c19ddf52.png">
          </a>
      </td>
      <td>    
        <ul>
         <li>User Login</li>
         <li>Add new consumer</li>      
         <li>View all consumers</li>
         <li>Delete a consumer</li>    
         <li>Modify Consumer</li>
         <li>Generate a Bill for a consumer</li>
        </ul>
        <p><b><a href="https://replit.com/@Prerit008/Electricity-Billing-System">Get started with Electricity Billing System!</a></b></p>
      </td>
    </tr>
   </tbody>
  </table>

---

## How It Works ❓

The code first establishes a connection to an ebs.sql SQLite3 database, and creates a table named consumer with the following fields:
- acc_no
- name
- addr
- contact
- P_cost
<br/>
The acc_no field is defined as an integer with a size of 4 and is set as the primary key for the table.

---

## Details about the Functions (Def) 🧩

1. The **login()** 🔐 function allows a user to login with a username and password. The only valid login is with the **username** '1' and **password** '1', and all other combinations will result in an error message being printed.

2. The **list_consumers()** 📃 function lists all consumers stored in the consumer table by executing a **SELECT** query and printing the resulting records.

3. The **add_consumer()** ➕ function prompts the user for the fields of a new consumer and adds a new record to the consumer table with the provided information.

4. The **del_consumer()** ❌ function takes an acc_no as an argument and deletes the consumer with that account number from the consumer table.

5. The **modify_consumer()** ✅ function takes an acc_no as an argument and allows the user to modify the fields of the consumer with that account number in the consumer table.

6. The **generate_bill()** 🧾 function takes an acc_no as an argument and generates a bill for the consumer with that account number by retrieving the consumer's information and power consumption from the consumer table and calculating the total cost using a user-provided rate for power. The bill is then printed to the console.

Thank you! 😊 

---

## Requiements 💻

##### Python 3.5 or later + SQLLITE3
The code is written in Python, so you will need to have a compatible version of Python installed on your system in order to run it.

---

## Limitations 

There are a few potential drawbacks or limitations to the current implementation of this program:
- **Security** 🔑 : The login function uses hard-coded values for the username and password, which is not a secure way to authenticate users. It would be better to use a more secure authentication method, such as prompting the user for their login credentials and storing hashed versions of these credentials in the database.

- **User input validation** 👨‍💼 : The program does not currently perform any validation on user input, which could lead to issues if the user provides invalid or malformed input. For example, the add_consumer and modify_consumer functions assume that the user will always provide valid integer values for the vacc_no, vcontact, and vP_cost variables. If the user provides a non-integer value, the program will raise a ValueError exception.

- **Error handling** ⚠️ : The program does not include any error handling code to handle exceptions or errors that may occur during execution. For example, if the database connection fails or if the program is unable to execute a SQL query, it will simply raise an exception and terminate. It would be better to include error handling code to handle these types of issues gracefully and provide more user-friendly error messages.

- **Code organization** 🌐 : The code in this program could be organized in a more modular and scalable way. Currently, all of the functions are defined in a single script, which could make it difficult to maintain and modify the code in the future. It might be helpful to split the code into separate modules or functions and use appropriate object-oriented design principles to make the code more maintainable and extensible.
