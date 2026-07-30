-- ============================================
-- SMART HEALTHCARE PLATFORM
-- Week 1 - Day 7
-- Insert Sample Data
-- ============================================

INSERT INTO Patients
(first_name, last_name, gender, age, phone, email, blood_group, address, registration_date)
VALUES
('Rahul','Sharma','Male',30,'9876543210','rahul@gmail.com','O+','Chennai','2026-07-30'),
('Priya','Kumar','Female',25,'9876543211','priya@gmail.com','A+','Salem','2026-07-30'),
('Arun','Raj','Male',41,'9876543212','arun@gmail.com','B+','Coimbatore','2026-07-30'),
('Divya','S','Female',35,'9876543213','divya@gmail.com','AB+','Erode','2026-07-30'),
('Karthik','R','Male',28,'9876543214','karthik@gmail.com','O-','Namakkal','2026-07-30');

INSERT INTO Doctors
(first_name, last_name, specialization, phone, email, experience, department)
VALUES
('Ramesh','K','Cardiologist','9876500001','ramesh@hospital.com',15,'Cardiology'),
('Meena','P','Neurologist','9876500002','meena@hospital.com',12,'Neurology'),
('Suresh','M','Orthopedic','9876500003','suresh@hospital.com',10,'Orthopedics'),
('Anitha','R','Dermatologist','9876500004','anitha@hospital.com',8,'Dermatology'),
('Vijay','S','Pediatrician','9876500005','vijay@hospital.com',14,'Pediatrics');