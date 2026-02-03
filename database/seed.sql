-- Seed data for all databases whilst testing
INSERT INTO users
(username, email, password)
VALUES
('admin', 'admin@example.com', 'admin123'),
('user1', 'user1@example.com', 'password1'),
('user2', 'user2@example.com', 'password2'),
('user3', 'user3@example.com', 'password3'),
('user4', 'user4@example.com', 'password4'),
('test', 'test@test.com', 'test');

INSERT INTO technicians
(technican_id, name, department)
VALUES
(1, 'Tech One', 'EV Specialist'),
(2, 'Tech Two', 'General Maintenance'),
(3, 'Tech Three', 'Solar Specialist'),
(4, 'Test', 'Test');

INSERT INTO bookings
(booking_id, user_id, address, booking_date, booking_time, booking_type, booking_status, technican_id)
VALUES
(1, 2, 'Middlesbrough', '2024-07-01', '10:00', 'EV Charger Installation', 'Pending', 1),
(2, 3, 'Billingham',  '2024-07-02', '14:00', 'Solar Pannel Maintenance', 'Confirmed', 2),
(3, 4, 'Stockton-On-Tees',  '2024-07-03', '09:00', 'Energy Management Repair', 'Completed', 3),
(4, 5, 'Newcastle',  '2024-07-04', '11:30', 'EV Charger Repair', 'Pending', 1),
(5, 2, 'Acklam',  '2024-07-05', '15:00', 'Solar Pannel Installation', 'Confirmed', 3);

INSERT INTO salesmenAppointments
(name, email, appoint_reason)
VALUES
('John', 'john123@gmail.com', 'Enquire about solar pannels installation.'),
('Bob', 'bob321@gmail.com', 'Wanting to replace current EV Charger.');