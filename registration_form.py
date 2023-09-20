import mysql.connector
import streamlit as st
import pandas as pd

# Establish a connection to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sabita@1234",
    database="icvadatabase"
)

# Streamlit app
st.title('ICVA Database Viewer')

# Function to fetch and display table data
def view_table(table_name):
    try:
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, con=mydb)
        st.write(f"Displaying data from the {table_name} table:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# List of tables in the database
tables = ['Language', 'Subjects', 'Classes', 'Exams', 'Organizations', 'Experts',
          'Questions', 'Answers', 'ExamPaper', 'MCQPaperSet', 'PaperSet', 'Country',
          'State', 'District', 'Subdivision', 'Students', 'Courses']

# Select a table to view
selected_table = st.selectbox('Select a table to view:', tables)

# View the selected table
view_table(selected_table)






mycursor = mydb.cursor()


# Streamlit app title
st.title("Database Interaction App")

# Select the table to interact with
selected_table = st.selectbox("Select a table:", ("Language", "Subjects","Classes","Exams","Organizations",'Experts',
          'Questions', 'Answers', 'ExamPaper', 'MCQPaperSet', 'PaperSet', 'Country',
          'State', 'District', 'Subdivision', 'Students', 'Courses'))  # Add more table names if needed

# Function to insert data into the Language table
def insert_language_data():
    st.header("Insert Data into Language Table")
    name = st.selectbox("Name", ("ENGLISH", "BENGALI", "HINDI"), key="language_name_selectbox")
    short_name = st.selectbox("Short Name", ("ENG", "BEN", "HIN"), key="language_short_name_selectbox")

    if st.button("Insert"):
        insert_query = "INSERT INTO Language (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Language data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Language table
def display_language_table():
    st.header("Language Table")
    mycursor.execute("SELECT * FROM Language")
    data = mycursor.fetchall()
    st.write(data)
    
    

# Function to insert data into the Subjects table
def insert_subject_data():
    st.header("Insert Data into Subjects Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Subjects (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Subject data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Subjects table
def display_subjects_table():
    st.header("Subjects Table")
    mycursor.execute("SELECT * FROM Subjects")
    data = mycursor.fetchall()
    st.write(data)
    
    

# Function to insert data into the Classes table
def insert_class_data():
    st.header("Insert Data into Classes Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Classes (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Class data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Classes table
def display_classes_table():
    st.header("Classes Table")
    mycursor.execute("SELECT * FROM Classes")
    data = mycursor.fetchall()
    st.write(data)
    
    
# Function to insert data into the Exams table
def insert_exam_data():
    st.header("Insert Data into Exams Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Exams (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Exam data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Exams table
def display_exams_table():
    st.header("Exams Table")
    mycursor.execute("SELECT * FROM Exams")
    data = mycursor.fetchall()
    st.write(data)
    

# Function to insert data into the Organizations table
def insert_organization_data():
    st.header("Insert Data into Organizations Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")
    org_type = st.selectbox("Type", ("Govt", "Private", "Govt Aided", "NGO", "Govt Under Taken", "Public"))
    address = st.text_area("Address")

    if st.button("Insert"):
        insert_query = "INSERT INTO Organizations (Name, ShortName, Type, Address) VALUES (%s, %s, %s, %s)"
        values = (name, short_name, org_type, address)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Organization data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Organizations table
def display_organizations_table():
    st.header("Organizations Table")
    mycursor.execute("SELECT * FROM Organizations")
    data = mycursor.fetchall()
    st.write(data)
    
# Function to insert data into the Experts table
def insert_expert_data():
    st.header("Insert Data into Experts Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")
    organization_id = st.number_input("Organization ID", min_value=1)
    permanent_address = st.text_area("Permanent Address")
    communication_address = st.text_area("Communication Address")
    qualification = st.text_area("Qualification")
    designation = st.text_input("Designation", value="TEACHER")
    experience = st.text_area("Experience")
    joining_date = st.date_input("Joining Date")

    if st.button("Insert"):
        insert_query = "INSERT INTO Experts (Name, ShortName, OrganizationID, ParmanentAddress, CommunicationAddress, Qualification, Designation, Experience, JoiningDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, short_name, organization_id, permanent_address, communication_address, qualification, designation, experience, joining_date)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Expert data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Experts table
def display_experts_table():
    st.header("Experts Table")
    mycursor.execute("SELECT * FROM Experts")
    data = mycursor.fetchall()
    st.write(data)
    
# Function to insert data into the Questions table
def insert_question_data():
    st.header("Insert Data into Questions Table")
    expert_id = st.number_input("Expert ID", min_value=1, step=1)
    que_beng_text = st.text_area("Bengali Text")
    que_eng_text = st.text_area("English Text")

    if st.button("Insert"):
        insert_query = "INSERT INTO Questions (ExprtID, QueBengText, QueEngText) VALUES (%s, %s, %s)"
        values = (expert_id, que_beng_text, que_eng_text)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Question data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Questions table
def display_questions_table():
    st.header("Questions Table")
    mycursor.execute("SELECT * FROM Questions")
    data = mycursor.fetchall()
    st.write(data)


# Function to insert data into the Answers table
def insert_answer_data():
    st.header("Insert Data into Answers Table")
    ques_id = st.number_input("Question ID", min_value=1, step=1)
    expert_id = st.number_input("Expert ID", min_value=1, step=1)
    ans_beng_text = st.text_area("Bengali Text")
    ans_eng_text = st.text_area("English Text")

    if st.button("Insert"):
        insert_query = "INSERT INTO Answers (QuesID, ExprtID, AnsBengText, AnsEngText) VALUES (%s, %s, %s, %s)"
        values = (ques_id, expert_id, ans_beng_text, ans_eng_text)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Answer data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Answers table
def display_answers_table():
    st.header("Answers Table")
    mycursor.execute("SELECT * FROM Answers")
    data = mycursor.fetchall()
    st.write(data)
    
# Function to insert data into the ExamPaper table
def insert_exam_paper_data():
    st.header("Insert Data into ExamPaper Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")
    exam_id = st.number_input("Exam ID", min_value=1, step=1)
    class_id = st.number_input("Class ID", min_value=1, step=1)
    subj_id = st.number_input("Subject ID", min_value=1, step=1)
    expert_id = st.number_input("Expert ID", min_value=1, step=1)
    full_marks = st.number_input("Full Marks", min_value=0, step=1)

    if st.button("Insert"):
        insert_query = "INSERT INTO ExamPaper (Name, ShortName, ExamID, ClassID, SubjID, ExprtID, FullMarks) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, short_name, exam_id, class_id, subj_id, expert_id, full_marks)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("ExamPaper data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the ExamPaper table
def display_exam_paper_table():
    st.header("ExamPaper Table")
    mycursor.execute("SELECT * FROM ExamPaper")
    data = mycursor.fetchall()
    st.write(data)
    
# Function to insert data into the MCQPaperSet table
def insert_mcq_data():
    st.header("Insert Data into MCQPaperSet Table")
    ques_id = st.number_input("Question ID", min_value=1, step=1)
    exam_paper_id = st.number_input("Exam Paper ID", min_value=1, step=1)
    lang_id = st.number_input("Language ID", min_value=1, step=1)
    option1 = st.text_input("Option 1")
    option2 = st.text_input("Option 2")
    option3 = st.text_input("Option 3")
    option4 = st.text_input("Option 4")
    marks = st.number_input("Marks", min_value=1, step=1)
    harder_rank = st.number_input("Harder Rank", min_value=1, max_value=4, step=1)

    if st.button("Insert"):
        insert_query = "INSERT INTO MCQPaperSet (QuesID, ExamPaperID, LangID, Option1, Option2, Option3, Option4, Marks, HarderRank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (ques_id, exam_paper_id, lang_id, option1, option2, option3, option4, marks, harder_rank)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("MCQ data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the MCQPaperSet table
def display_mcq_table():
    st.header("MCQPaperSet Table")
    mycursor.execute("SELECT * FROM MCQPaperSet")
    data = mycursor.fetchall()
    st.write(data)
    

# Function to insert data into the PaperSet table
def insert_paper_set_data():
    st.header("Insert Data into PaperSet Table")
    ques_id = st.number_input("Question ID", min_value=1, step=1)
    exam_paper_id = st.number_input("Exam Paper ID", min_value=1, step=1)
    lang_id = st.number_input("Language ID", min_value=1, step=1)
    marks = st.number_input("Marks", min_value=0, step=1)
    harder_rank = st.number_input("Harder Rank", min_value=0, max_value=9, step=1)

    if st.button("Insert"):
        insert_query = "INSERT INTO PaperSet (QuesID, ExamPaperID, LangID, Marks, HarderRank) VALUES (%s, %s, %s, %s, %s)"
        values = (ques_id, exam_paper_id, lang_id, marks, harder_rank)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("PaperSet data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the PaperSet table
def display_paper_set_table():
    st.header("PaperSet Table")
    mycursor.execute("SELECT * FROM PaperSet")
    data = mycursor.fetchall()
    st.write(data)        


# Function to insert data into the Country table
def insert_country_data():
    st.header("Insert Data into Country Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Country (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Country data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Country table
def display_country_table():
    st.header("Country Table")
    mycursor.execute("SELECT * FROM Country")
    data = mycursor.fetchall()
    st.write(data)
        
# Function to insert data into the State table
def insert_state_data():
    st.header("Insert Data into State Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO State (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("State data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the State table
def display_state_table():
    st.header("State Table")
    mycursor.execute("SELECT * FROM State")
    data = mycursor.fetchall()
    st.write(data)
            
# Function to insert data into the District table
def insert_district_data():
    st.header("Insert Data into District Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO District (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("District data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the District table
def display_district_table():
    st.header("District Table")
    mycursor.execute("SELECT * FROM District")
    data = mycursor.fetchall()
    st.write(data)
    
    
# Function to insert data into the Subdivision table
def insert_subdivision_data():
    st.header("Insert Data into Subdivision Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Subdivision (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Subdivision data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Subdivision table
def display_subdivision_table():
    st.header("Subdivision Table")
    mycursor.execute("SELECT * FROM Subdivision")
    data = mycursor.fetchall()
    st.write(data)
    
def insert_student_data():
    st.header("Insert Data into Students Table")
    fname = st.text_input("First Name")
    mname = st.text_input("Middle Name")
    lname = st.text_input("Last Name")
    title = st.selectbox("Title", ("Mr.", "Mrs.", "Master", "Miss", "Sri", "Sk", "Dr."))
    father_name = st.text_input("Father Name")
    mother_name = st.text_input("Mother Name")
    class_id = st.selectbox("Class", ("001 - CLASS SEVEN", "002 - CLASS EIGHT"))
    gender = st.selectbox("Gender", ("FEMALE", "MALE", "TRANSGENDER"))
    doa = st.date_input("Date of Admission")
    p_address = st.text_area("Permanent Address")
    p_subdiv_id = st.selectbox("Permanent Subdivision", (1, 2, 3))
    p_dist_id = st.selectbox("Permanent District", (1, 2, 3))
    p_state_id = st.selectbox("Permanent State", (1, 2, 3))
    p_country_id = st.selectbox("Permanent Country", (1, 2, 3))
    p_pin_code = st.number_input("Permanent Pin Code", min_value=100000, max_value=9999999)
    c_address = st.text_area("Communication Address")
    c_subdiv_id = st.selectbox("Communication Subdivision", (1, 2, 3))
    c_dist_id = st.selectbox("Communication District", (1, 2, 3))
    c_state_id = st.selectbox("Communication State", (1, 2, 3))
    c_country_id = st.selectbox("Communication Country", (1, 2, 3))
    c_pin_code = st.number_input("Communication Pin Code", min_value=100000, max_value=9999999)
    email_address = st.text_input("Email Address")
    alt_email_address = st.text_input("Alternate Email Address")
    mobile_no = st.number_input("Mobile No", min_value=1000000000, max_value=9999999999)
    alt_mobile_no = st.number_input("Alternate Mobile No", min_value=1000000000, max_value=9999999999)

    if st.button("Insert"):
        insert_query = "INSERT INTO Students (FName, MName, LName, Title, FatherName, MotherName, ClassID, Gender, DoA, PAddress, PSubDivID, PDistID, PStateID, PCountryID, PPinCode, CAddress, CSubDivID, CDistID, CStateID, CCountryID, CPinCode, EmailAddress, AltEmailAddress, MobileNo, AltMobileNo) " \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            fname, mname, lname, title, father_name, mother_name, class_id.split(" - ")[0], gender, doa, p_address,
            p_subdiv_id, p_dist_id, p_state_id, p_country_id, p_pin_code, c_address, c_subdiv_id, c_dist_id, c_state_id,
            c_country_id, c_pin_code, email_address, alt_email_address, mobile_no, alt_mobile_no
        )

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Student data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")
# Function to display the Students table
def display_students_table():
    st.header("Students Table")
    mycursor.execute("SELECT * FROM Students")
    data = mycursor.fetchall()
    st.write(data)
    

# Function to insert data into the Courses table
def insert_course_data():
    st.header("Insert Data into Courses Table")
    course_name = st.text_input("Course Name")
    course_short_name = st.text_input("Course Short Name")
    
    if st.button("Insert"):
        insert_query = "INSERT INTO Courses (Name, ShortName) VALUES (%s, %s)"
        values = (course_name, course_short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Course data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# Function to display the Courses table
def display_courses_table():
    st.header("Courses Table")
    mycursor.execute("SELECT * FROM Courses")
    data = mycursor.fetchall()
    st.write(data)
        
                
# Check the selected table and perform actions accordingly
if selected_table == "Language":
    insert_language_data()
    display_language_table()
    
elif selected_table == "Subjects":
    insert_subject_data()
    display_subjects_table()
    
elif selected_table == "Classes":
    insert_class_data()
    display_classes_table()    

elif selected_table == "Exams":
    insert_exam_data()
    display_exams_table()
    
elif selected_table == "Organizations":
    insert_organization_data()
    display_organizations_table() 
    
elif selected_table == "Experts":
    insert_expert_data()
    display_experts_table()     
 
 
elif selected_table == "Questions":   
    insert_question_data()
    display_questions_table()  
    
elif selected_table == "Answers":
    insert_answer_data()
    display_answers_table()    
    
elif selected_table == "ExamPaper":
    insert_exam_paper_data()
    display_exam_paper_table()
    
elif selected_table == "MCQPaperSet":
    insert_mcq_data()
    display_mcq_table()        


elif selected_table == "PaperSet":
    insert_paper_set_data()
    display_paper_set_table()


elif selected_table == "Country":
    insert_country_data()
    display_country_table()    
    
elif selected_table == "State":  
    insert_state_data()
    display_state_table()    


elif selected_table == "District":  # Add this condition for the District table
    insert_district_data()
    display_district_table()


elif selected_table == "Subdivision":  # Add this condition for the Subdivision table
    insert_subdivision_data()
    display_subdivision_table()
    
elif selected_table == "Students":  # Add this condition for the Students table
    insert_student_data()
    display_students_table()    
    
elif selected_table == "Courses":  # Add this condition for the Courses table
    insert_course_data()
    display_courses_table()    
    
           
# Close database connection
mycursor.close()
mydb.close()