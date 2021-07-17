# AzentCollegeSearch

>Azent College List (Backend)

The backend is associated with MongoDB as the database. The model includes all the fields mentioned as part of the document —>

<img width="695" alt="country" src="https://user-images.githubusercontent.com/43857930/126038566-49477dab-1f88-4cc6-9759-c50dd21ed54d.png">

Single URL is used as the API for searching in this case since it is a small application. The user searches are directly read from the URL (a body is not being passed in this case), and being matched to the appropriate fields to find the nearest match 

<img width="805" alt="If country code is not None" src="https://user-images.githubusercontent.com/43857930/126038575-96d1775c-7c73-4539-85c0-a819876aa0cf.png">

The output allows the user to search across name, domain, and alpha_two_code.

<img width="840" alt="Screenshot 2021-07-17 at 6 19 11 PM" src="https://user-images.githubusercontent.com/43857930/126038582-41e9dd25-ec3b-4c21-8b92-284dd614b0aa.png">

<img width="1440" alt="Screenshot 2021-07-17 at 6 36 09 PM" src="https://user-images.githubusercontent.com/43857930/126038587-2d7ab145-5d05-417d-8d54-5ff2d410d54a.png">



>Azent College View (Frontend)

The front end is made on react. This particular use case did not need navigation so the entire app is an SPA, with two main components i.e. Header and Landing. 

### Header

The header is is a simple div with Azent logo in the centre. The header is rounded at the bottom edges and given a box shadow to bring out an added dimension

### Landing

The Landing page is mainly broken down into 2 main sections, i.e. the search area and the cards displaying the college details. 

<img width="1440" alt="Screenshot 2021-07-17 at 5 59 19 PM" src="https://user-images.githubusercontent.com/43857930/126038601-63341693-67f8-4b13-a17f-5709fd4176fe.png">


#### Search Area

The search area provides filtering options to the user to either search by keywords i.e. user input or by filters. The filters are categorised as Country  and Domain. These fields are populated when the components are mounted. Each time the search option using the input is triggered the checkboxes are updated to keep in sync with the keyword search.

<img width="1440" alt="Screenshot 2021-07-17 at 6 29 46 PM" src="https://user-images.githubusercontent.com/43857930/126038608-b5440386-fa07-4cdd-8d6f-2bbfab9a2f67.png">

When changes are made using the filters, it is made sure that the API call does not change the checkboxes. This is done to maintain options. It is also the reason 2 separate arrays are created, to avoid the above mentioned scenario. 

<img width="1440" alt="Screenshot 2021-07-17 at 6 02 15 PM" src="https://user-images.githubusercontent.com/43857930/126038615-ca959078-8369-42c0-960f-825e7cd6e4cd.png">

<img width="1440" alt="Screenshot 2021-07-17 at 6 02 30 PM" src="https://user-images.githubusercontent.com/43857930/126038619-abcaab8b-deab-4078-8175-08d8b681fd30.png">
