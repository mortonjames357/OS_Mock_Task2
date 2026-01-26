INSERT INTO users
(user_id, username, email, password)
VALUES
(1, 'admin', 'admin@example.com', 'admin123'),
(2, 'user1', 'user1@example.com', 'password1'),
(3, 'user2', 'user2@example.com', 'password2'),
(4, 'user3', 'user3@example.com', 'password3'),
(5, 'user4', 'user4@example.com', 'password4');


INSERT INTO bookings
(booking_id, user_id, booking_date, booking_time, booking_type, booking_status, technican_id)
VALUES
(1, 2, '2024-07-01', '10:00', 'EV Charger Installation', 'Pending', 1),
(2, 3, '2024-07-02', '14:00', 'Solar Pannel Maintenance', 'Confirmed', 2),
(3, 4, '2024-07-03', '09:00', 'Energy Management Repair', 'Completed', 3),
(4, 5, '2024-07-04', '11:30', 'EV Charger Repair', 'Pending', 1),
(5, 2, '2024-07-05', '15:00', 'Solar Pannel Installation', 'Confirmed', 3);


INSERT INTO technicians
(technican_id, name, expertise)
VALUES
(1, 'Tech One', 'EV Specialist'),
(2, 'Tech Two', 'General Maintenance'),
(3, 'Tech Three', 'Solar Specialist');
