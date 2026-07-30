-- =====================================
-- SMART HEALTHCARE PLATFORM
-- Week 1 - Day 5
-- Patients & Doctors Tables
-- =====================================

CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    age INT,
    phone VARCHAR(20),
    email VARCHAR(100),
    blood_group VARCHAR(10),
    address TEXT,
    registration_date DATE
);

CREATE TABLE Doctors (
    doctor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialization VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    experience INT,
    department VARCHAR(100)
);