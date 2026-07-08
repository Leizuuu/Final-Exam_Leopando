# Migration Report

## Legacy Architecture
The original application was treated as a monolithic system.

## C4 Level 2 Container Diagram
(Add your diagram here or an image reference.)

## Code Smells
1. God Object
2. Hardcoded Coupling
3. Lack of Separation of Concerns

## Refactoring
The monolithic design was migrated into a microservice-inspired structure:
- Authentication Service
- Data Processing Service
- Factory Service

## Design Patterns
- Factory Pattern for dynamic service discovery.
- Strategy Pattern for encryption and compression.

## Manual Verification
- Verified the encryption strategy using XOR key `0x4F`.
- Verified the compression strategy using factor `0.85`.
- Confirmed that the application executed successfully after testing.

## JWT Cryptographic Handshake

The authentication service uses JSON Web Tokens (JWT) with the HS256 algorithm.

Authentication process:

1. The user submits login credentials.
2. The server validates the credentials.
3. If valid, the server creates a JWT containing user information and an expiration time.
4. The JWT is digitally signed using the application's secret key.
5. The client stores the JWT and sends it with future requests.
6. The server verifies the signature before granting access to protected resources.

This mechanism ensures message integrity and verifies that the token has not been modified.