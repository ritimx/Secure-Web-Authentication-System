# Secure Web Authentication System

## Authentication & Authorization Flow
This system implements a secure authentication and authorization flow to ensure user data protection and secure access control. Below are the key components:

1. **Authentication**:
   - Users can register with a username, email, and password.
   - Passwords are hashed using `werkzeug.security`'s `generate_password_hash` function before being stored in the database.
   - During login, the provided password is verified using `check_password_hash`.

2. **Authorization**:
   - After successful login, a session is created for the user.
   - Access to the dashboard and other protected routes is restricted to authenticated users only.
   - Unauthorized users are redirected to the login page.

3. **Input Validation & Sanitization**:
   - All user inputs are validated on the client-side using HTML5 attributes (e.g., `required`, `type="email"`).
   - Server-side validation ensures that malicious inputs are sanitized before processing.

4. **Session Handling & Access Control**:
   - Sessions are securely managed using Flask's session mechanism.
   - The `app.secret_key` is used to sign session cookies, ensuring their integrity.
   - Users can log out, which clears their session data.

## Deliverables

1. **Complete Source Code**:
   - The complete source code is available in this repository.
   - The project is implemented using Python (Flask framework) and SQLite for the database.

2. **Security Design Explanation**:
   - Passwords are hashed using a secure hashing algorithm to prevent plaintext storage.
   - Input validation and sanitization are implemented to prevent SQL injection and XSS attacks.
   - Sessions are securely managed to prevent unauthorized access.

3. **README with Screenshots & Flow**:
   - Below are screenshots of the application:

### Login Page
![Login Page](screenshots/login.png)

### Register Page
![Register Page](screenshots/register.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

4. **Flow**:
   - **Step 1**: User registers with a username, email, and password.
   - **Step 2**: User logs in with their email and password.
   - **Step 3**: Upon successful login, the user is redirected to the dashboard.
   - **Step 4**: The dashboard displays user-specific information and provides access to logs, users, and settings.
   - **Step 5**: The user can log out, which clears their session and redirects them to the login page.

## How to Run the Application

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd Secure-Web-Authentication-System
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Security Best Practices

- Use HTTPS in production to encrypt data in transit.
- Regularly update dependencies to patch known vulnerabilities.
- Implement rate limiting to prevent brute force attacks.
- Use environment variables to store sensitive information like `app.secret_key`.
- Regularly audit and test the application for security vulnerabilities.

---

For any questions or issues, feel free to open an issue or contact the repository maintainer.