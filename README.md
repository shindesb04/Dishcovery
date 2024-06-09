# dishCovery
Using CNN to Identify Vegetables or Fruits and Suggest Recipes
________________________________________________________________________________________________________________________________
This video encapsulates the fruition of our efforts, showcasing the project outcome in its entirety.
https://github.com/rohitroy1711/dishCovery/assets/63733152/60c521aa-62ed-4c66-9086-eafc804a1b3b
________________________________________________________________________________________________________________________________

Login Page - The login page features two text fields where users can input their email address and password. Once the user fills in both fields, they can proceed by clicking the "Login" button. This login page can be used as a template or integrated into various web applications to facilitate user authentication. If you encounter any issues or have suggestions for improvement, please don't hesitate to open an issue or submit a pull request.

<img width="960" alt="Screenshot 2024-02-06 174402" src="https://github.com/rohitroy1711/dishCovery/assets/63733152/fe933214-0d33-4141-a981-1130e318aea7">
________________________________________________________________________________________________________________________________

Signup Page - The signup page features fields for users to input their first name, last name, email address, and password. Once users have filled in all required fields, they can proceed by clicking the "Register" button to create an account.

This signup page can be integrated into various web applications to facilitate user registration processes. It provides a simple and intuitive interface for users to input their information securely. Developers can customize the page according to their project's requirements, adding additional fields or validation as needed.
<img width="949" alt="Screenshot 2024-02-06 174502" src="https://github.com/rohitroy1711/dishCovery/assets/63733152/1a1d49e0-3dbb-4443-95b4-dd39122bc254">
________________________________________________________________________________________________________________________________
Database - 
  This repository contains the configuration and setup instructions for storing user registration details in MongoDB Compass. MongoDB Compass is a graphical user interface (GUI) tool designed to interact with MongoDB databases.

After a user successfully registers through the signup page, their details are stored in MongoDB Compass. The database schema includes fields such as first name, last name, email address, and password, allowing for efficient storage and retrieval of user information.

To set up MongoDB Compass for storing user details, follow these steps:

Install MongoDB Compass: Download and install MongoDB Compass from the official MongoDB website (https://www.mongodb.com/try/download/compass).

Configure Connection: Launch MongoDB Compass and configure the connection to your MongoDB database. This typically involves providing the connection string or specifying the host, port, and authentication credentials.

Create Database: Create a new database in MongoDB Compass to store user details. Define the database name and any required collections or indexes.

Define Schema: Define the schema for storing user details, including fields such as first name, last name, email address, and password. Ensure appropriate data types and validation rules are applied to maintain data integrity.

Implement CRUD Operations: Implement Create, Read, Update, and Delete (CRUD) operations in your application to interact with MongoDB Compass. Use the appropriate MongoDB driver for your programming language to perform database operations.

By following these steps, you can effectively store user registration details in MongoDB Compass, providing a reliable and scalable solution for managing user data in your application.

If you encounter any difficulties or have questions about configuring MongoDB Compass, refer to the MongoDB documentation or seek assistance from the MongoDB community.

**Image of Mongodb Compass where all the registered user details are stored**

<img width="960" alt="Screenshot 2024-02-06 182134" src="https://github.com/rohitroy1711/dishCovery/assets/63733152/f819cda1-d2c7-46fa-9454-58184e2c786d">
________________________________________________________________________________________________________________________________


Login: Upon successful login, you'll be redirected to the home page.

Upload Image: You can upload an image of a fruit or vegetable. Once uploaded, our trained Convolutional Neural Network (CNN) model will predict what fruit or vegetable it is.
<img width="960" alt="Screenshot 2024-02-06 180029" src="https://github.com/rohitroy1711/dishCovery/assets/63733152/99b1bbd1-3607-439f-9c3d-d3724dcb0640">

Prediction Result: After the image is processed, you'll be redirected to the next page where the predicted fruit or vegetable's name will be displayed in a text box. You can also manually add more vegetables or fruits to the text box.
<img width="960" alt="Screenshot 2024-02-06 180121" src="https://github.com/rohitroy1711/dishCovery/assets/63733152/88b4094b-cc14-4f64-bb1c-b26627b88a54">
<img width="960" alt="Screenshot 2024-02-06 180217" src="https://github.com/rohitroy1711/dishCovery/assets/63733152/6808b608-f80a-4059-80c5-403e89c00669">


Submit: Upon clicking the "Submit" button, you'll be redirected to a new webpage showing the top 3 dishes you can make with the selected vegetables or fruits.
<img width="960" alt="Screenshot 2024-02-06 180308" src="https://github.com/rohitroy1711/dishCovery/assets/63733152/f3aa2ac5-2502-4cde-9dc6-4b9be4a37e65">

Select Dish: From the list of dishes, you can select one. If selected, the webpage will display the remaining ingredients and the process of making that dish.
<img width="960" alt="Screenshot 2024-02-06 180352" src="https://github.com/rohitroy1711/dishCovery/assets/63733152/5dc1afef-5518-424d-9f35-9a8450a0465d">

No Recipes Found: If there are no recipes available for the selected vegetables or fruits, the webpage will display a message indicating "No recipes found."

Our application aims to provide you with culinary inspiration based on the vegetables or fruits you upload. Whether you're looking to explore new dishes or utilize ingredients you have on hand, we're here to assist you in your cooking endeavors.

Thank you for using our web application, and happy cooking!


