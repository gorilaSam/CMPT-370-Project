from PatientProfile import *
import Demographics, Labwork, Medication, MedicationsList, Names, Note, Allergy, AllergyList
import sqlite3

class DatabaseController():

    def create_connection(self):
        """ 
        creates a database connection to the SQLite database
        :param db_file: database file
        :return: Connection object or None
        """
        db = None
        try:
            db = sqlite3.connect('./db/medical.db')
        except Exception as e:
            print(e)
        return db

    #currently unused  
    def execute_insert_query(self, health_num, table_name, column_name, value):
        db = self.create_connection()
        cur = db.cursor()
        cur.execute("INSERT OR REPLACE INTO "+table_name+" (patientID, "+column_name+") VALUES (?, ?)", (health_num, value))
        cur.close()
        db.commit()
        db.close()

    def post_row(self, health_num, table_name, dict):
        """
        Given the relevant patient's health card number, insert or REPLACE a dictionary as a row of information
        into the provided data table
        :param health_num: a 9-digit integer health number corresponding to patient
        :param table_name: name of the data table to be inserted into
        :param dict: dictionary containing the fields of information to be inserted
        """
        #Setup db connect
        db = self.create_connection()
        cur = db.cursor()
        #transform dict into params for query
        keys = ','.join(dict.keys())
        question_marks = ','.join(list('?'*((len(dict))+1)))
        values = list(dict.values())
        #insert health_num as first value in query (It is always the primary key)
        values.insert(0, health_num)
        #Execute the query
        try:
            cur.execute('INSERT OR REPLACE INTO '+table_name+' (patientID, '+keys+') VALUES ('+question_marks+')', values)
            db.commit()
        except Exception as e:
            print(e)
        #finishing up
        cur.close()
        db.close()

    def get_patient(self, health_num):
        """
        Queries all the patient data from the database and compiles it into
        a patient object which is returned to the caller
        :param health_num: a 9-digit integer health number corresponding to patient
        :return PatientProfile: A PatientProfile object
        """
        patient_dict = {}
        patient_dict['full_name'] = self.get_name(health_num)
        patient_dict['demographics'] = self.get_demographics(health_num)
        patient_dict['notes'] = self.get_notes(health_num)          
        patient_dict['billing_code'] = self.get_billing(health_num)
        patient_dict['medications'] = self.get_medications(health_num)
        patient_dict['allergies'] = self.get_allergies(health_num)
        patient_dict['lab_work'] = None
        #Construct PatientProfile w/ dictionary
        patient_profile = PatientProfile(**patient_dict)
        return patient_profile

    def get_name(self, health_num):
        """
        Returns the fullname of the patient with that health number
        :param health_num: 9 digit int
        :return FullName: FullName object representing patient's name
        """
        db = self.create_connection()
        cur = db.cursor()
        query = """
            SELECT givenName, middleNames, surname FROM Names
            WHERE patientID = ?
        """
        try:
            cur.execute(query, (health_num,))
        except Exception as e:
            print(e)
        names = cur.fetchall()
        db.close()
        fn = FullName()
        fn.set_given_name(names[0][0])
        fn.set_middle_names([names[0][1]])
        fn.set_surname(names[0][2])
        return fn

    def get_demographics(self, health_num):
        """
        Returns the demographics of the patient with that health number
        :param health_num: 9 digit int
        :return Demographics: Demographics object containing patient information
        """
        db = self.create_connection()
        cur = db.cursor()
        query = """
            SELECT dateOfBirth, address, familyHistory, medicalConditions FROM Patient
            WHERE patientID = ?
        """
        try:
            cur.execute(query, (health_num,))
        except Exception as e:
            print(e)
        values = cur.fetchall()
        values_list = list(values[0])
        db.close()
        demo = Demographics.Demographics()
        demo.set_date_of_birth(values_list[0])
        demo.set_address(values_list[1])
        demo.set_family_history(values_list[2])
        demo.set_medical_conditions(values_list[3])
        return demo

    def get_notes(self, health_num):
        """
        Returns appended doctors note pertaining to patient
        :param health_num: 9 digit int
        :return Note[]: a list of Note objects
        """
        db = self.create_connection()
        cur = db.cursor()
        query = """
            SELECT * FROM Note
            WHERE patientID = ?
        """
        try:
            cur.execute(query, (health_num,))
        except Exception as e:
            print(e)
        values = cur.fetchall()
        list_of_notes = []
        for doc_note in values:
            note = Note.Note()
            date = doc_note[2].split('/')
            note.write_date(date[0], date[1], date[2])
            #Fix this later, maybe just change author in note to string
            fn = FullName()
            fn.set_given_name(doc_note[3])
            note.write_author(fn)
            note.write_body(doc_note[4])
            list_of_notes.append(note)
        return list_of_notes

    def get_billing(self, health_num):
        """
        Returns patient's billing code
        :param health_num: 9 digit int
        :return str: billing code
        """
        db = self.create_connection()
        cur = db.cursor()
        query = """
            SELECT billingCode FROM Billing
            WHERE patientID = ?
        """
        try:
            cur.execute(query, (health_num,))
        except Exception as e:
            print(e)
        values = cur.fetchall()
        db.close()
        return values[0][0]

    def get_medications(self, health_num):
        """
        Returns MedicationList pertaining to patient
        :param health_num: 9 digit int
        :return MedicationList: MedicationList datatype
        """
        db = self.create_connection()
        cur = db.cursor()
        query = """
            SELECT * FROM MedicationEntry
            WHERE patientID = ?
        """
        try:
            cur.execute(query, (health_num,))
        except Exception as e:
            print(e)
        values = cur.fetchall()
        med_list = MedicationsList.MedicationsList()
        for med in values:
            print(med)
            new_med = Medication.Medication(med[2], med[4], med[5], med[6], med[7])
            new_med.set_scientific_name(med[3])
            med_list.add_medication(new_med)
        db.close()
        return med_list

    def get_allergies(self, health_num):
        """
        Returns AllergyList correlated with the patient health number
        :param health_num: 9 digit int
        :return AllergyList: AllergyList object
        """
        db = self.create_connection()
        cur = db.cursor()
        query = """
            SELECT * FROM Allergies
            WHERE patientID = ?
        """
        try:
            cur.execute(query, (health_num,))
        except Exception as e:
            print(e)
        values = cur.fetchall()
        allergy_list = AllergyList.AllergyList()
        for allergy in values:
            new_allergy = Allergy.Allergy(allergy[2], allergy[3])
            allergy_list.add_allergy(new_allergy)
        db.close()
        return allergy_list

    def overwrite_patient(self, health_num, patient: PatientProfile):
        """
        Overwrites all the fields of a patient profile in the database or 
        creates one if it doesn't exist
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param PatientProfile: A PatientProfile object containing the new patient information
        """
        self.set_name(health_num, patient.profile['name'])

        self.set_demographics(health_num, patient.profile['demographics'])

        for note in patient.profile['notes']:
            self.insert_note(health_num, note)
 
        self.set_billing(health_num, patient.profile['billing_code'])

        self.set_medications(health_num, patient.profile['drugs'])

        self.set_allergies(health_num, patient.profile['allergies'])

        #self.set_lab_work(health_num, patient.profile['lab_work'])
    
    def set_name(self, health_num, fullname: FullName):
        """
        Writes the provided FullName objects information into the database for the
        given health_num
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param FullName: a FullName object containing the patient's name
        """
        full_name_dict = {}
        full_name_dict['givenName'] = fullname.get_given_name()
        full_name_dict['middleNames'] = fullname.get_middle_names_to_string()
        full_name_dict['surname'] = fullname.get_surname()   
        self.post_row(health_num, 'Names', full_name_dict)

    def set_demographics(self, health_num, demographics: Demographics):
        """
        Writes the information from the provided Demographics object into the database
        for the given health_num
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param demographics: a Demographics object containing patient information
        """
        self.post_row(health_num, 'Patient', demographics.demographics)
                 

    def insert_note(self, health_num, note: Note):
        """
        Inserts a note into the database for the specified patient
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param note: a Note object containing note information
        """
        db = self.create_connection()
        cur = db.cursor()
        cur.execute("INSERT INTO Note (patientID, date, author, body) VALUES (?, ?, ?, ?)", 
                    (health_num, note.get_date(), note.get_author(), note.get_body()))
        cur.close()
        db.commit()
        db.close()


    def set_billing(self, health_num, billing_code):
        """
        Writes the billing information into the database for the given patient
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param billing_code: a str representing patient billing code
        """
        db = self.create_connection()
        cur = db.cursor()
        try:
            cur.execute('INSERT OR REPLACE INTO Billing (patientID, billingCode) VALUES(?, ?)', 
                        (health_num, billing_code))
            db.commit()
        except Exception as e:
            print(e)
        db.close()


    def set_medications(self, health_num, medication_list: MedicationsList):
        """
        Writes/Replaces the provided medication list into the database for the patient.
        :param health_num: a 9-digit integer health number corresponding to patient 
        param medication_list: a MedicationsList object
        """

        #Remove existing medication values from table
        db = self.create_connection()
        cur = db.cursor()
        query = """
            DELETE FROM MedicationEntry
            WHERE patientID = ?
        """
        try:
            cur.execute(query, (health_num,))
            db.commit()
        except Exception as e:
            print(e)

        #NOTE: Market Names implementation not priority atm, use scientific name
        #Then replace with the updated List
        for drug in medication_list.medications:
            try:
                cur.execute("""INSERT INTO MedicationEntry(patientID, id, medicine_name, chemical_name, synonym, suppress) 
                VALUES(?, ?, ?, ?, ?, ?)""", (health_num, drug.id, drug.medicine_name, drug.chemical_name, drug.synonym, drug.suppress))
                db.commit()
            except Exception as e:
                print(e)
        
    def set_allergies(self, health_num, allergies: AllergyList):
        """
        Writes/Replaces the allergies list into the database for the specified patient
        :param health_num: a 9-digit integer health number corresponding to patient
        :param allergies: an Allergies object already containing allergy information
        """
        #Remove existing Allergy values from table
        db = self.create_connection()
        cur = db.cursor()
        query = """
            DELETE FROM Allergies
            WHERE patientID = ?
        """
        try:
            cur.execute(query, (health_num,))
            db.commit()
        except Exception as e:
            print(e)

        #Then replace with the updated List
        for allergy in allergies.allergy_list['allergies']:
            self.post_row(health_num, 'Allergies', allergy.allergy)



    def set_lab_work(self, health_num, lab_work: Labwork):
        """
        Writes the provided Lab work data into the database for the patient
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param lab_work: a LabWork object containing the lab work data in question
        """
        return


