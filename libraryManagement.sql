USE librarymanagement;

CREATE TABLE Members (
    MemberID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Phone VARCHAR(20),
    Address VARCHAR(255)
);

CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    AuthorName VARCHAR(255) NOT NULL,
    Nationality VARCHAR(100),
    DateOfBirth DATE
);

CREATE TABLE Publishers (
    PublisherID INT PRIMARY KEY AUTO_INCREMENT,
    PublisherName VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    ContactNumber VARCHAR(20)
);

CREATE TABLE Genres (
    GenreID INT PRIMARY KEY AUTO_INCREMENT,
    GenreName VARCHAR(100) NOT NULL,
    Description TEXT,
    SubGenre VARCHAR(100)
);

CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    AuthorID INT,
    GenreID INT,
    PublisherID INT,
    YearPublished INT,
    ISBN VARCHAR(20) UNIQUE,
    TotalCopies INT NOT NULL,
    AvailableCopies INT NOT NULL,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID),
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID),
    FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID)
);

CREATE TABLE Loans (
    LoanID INT PRIMARY KEY AUTO_INCREMENT,
    BookID INT,  
    MemberID INT,
    LoanDate DATE NOT NULL,
    ReturnDate DATE,
    DueDate DATE,
    Status ENUM('returned', 'overdue') NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);

CREATE TABLE Fines (
    FineID INT PRIMARY KEY AUTO_INCREMENT,
    LoanID INT,
    FineAmount DECIMAL(10, 2) NOT NULL,
    PaidStatus ENUM('paid', 'unpaid') NOT NULL,
    FOREIGN KEY (LoanID) REFERENCES Loans(LoanID)
);

CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT,
    BookID INT,
    MemberID INT,
    ReservationDate DATE NOT NULL,
    Status ENUM('active', 'fulfilled') NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
INSERT INTO Members (FullName, Email, Phone, Address)
VALUES
('Jane Doe', 'jane.doe@example.com', '08123456789', 'Jl. Sudirman'),
('John Smith', 'john.smith@example.com', '08223456789', 'Jl. Thamrin');

INSERT INTO Authors (AuthorName, Nationality, DateOfBirth)
VALUES
('George Orwell', 'British', '1903-06-25'),
('J.K. Rowling', 'British', '1965-07-31'),
('Ray Bradbury', 'American', '1920-08-22');


INSERT INTO Publishers (PublisherName, Address, ContactNumber)
VALUES
('Penguin Books', '375 Hudson St, New York, NY', '212-366-2000'),
('Bloomsbury Publishing', '50 Bedford Square, London', '020-7631-5600'),
('Simon & Schuster', '1230 Avenue of the Americas, New York, NY', '212-698-7401');

INSERT INTO Genres (GenreName, Description, SubGenre)
VALUES
('Fiction', 'Narrative works based on imagination', 'Historical Fiction'),
('Science Fiction', 'Fiction based on speculative science', 'Dystopian'),
('Non-Fiction', 'Works based on factual information', 'Biography');

INSERT INTO Books (Title, AuthorID, GenreID, PublisherID, YearPublished, ISBN, TotalCopies, AvailableCopies)
VALUES
('1984', 1, 2, 1, 1949, '9780451524935', 10, 8),
('Harry Potter and the Sorcerer''s Stone', 2, 1, 2, 1997, '9780439708180', 15, 12),
('Fahrenheit 451', 3, 2, 3, 1953, '9781451673319', 8, 5);

INSERT INTO Loans (BookID, MemberID, LoanDate, DueDate, ReturnDate, Status)
VALUES
(1, 1, '2024-09-20', '2024-10-05', '2024-10-03', 'returned'),
(2, 5, '2024-10-01', '2024-10-15', NULL, 'overdue'),
(3, 6, '2024-10-10', '2024-10-25', NULL, 'overdue');

INSERT INTO Fines (LoanID, FineAmount, PaidStatus)
VALUES
(2, 10.50, 'unpaid'),
(3, 7.00, 'unpaid');

SELECT * FROM Members;
SELECT * FROM Authors;
SELECT * FROM Publishers;
SELECT * FROM Genres;
SELECT * FROM Loans;
SELECT * FROM Books;



