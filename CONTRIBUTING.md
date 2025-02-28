# Contributing to CRONAI

Thank you for your interest in contributing to CRONAI! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## Branch Strategy

We use a structured branching strategy to manage development:

- `main` - The production branch, containing stable releases
- `develop` - The active development branch, where features are integrated
- Feature branches - For new features, named like `feature/your-feature-name`
- Bug fix branches - For bug fixes, named like `fix/bug-description`

## Development Workflow

1. **Fork the repository** (external contributors)
2. **Clone your fork or the main repository**:
   ```bash
   git clone https://github.com/yourusername/cronai.git
   cd cronai
   ```

3. **Create a new branch** from `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes** - Be sure to:
   - Follow the code style of the project
   - Add tests if applicable
   - Update documentation as needed

5. **Commit your changes** with clear messages:
   ```bash
   git commit -m "Add feature: short description of your changes"
   ```

6. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request** against the `develop` branch

## Pull Request Guidelines

When creating a pull request, please:

1. Fill out the pull request template
2. Reference any related issues
3. Include a summary of the changes and their purpose
4. Add screenshots for UI changes if applicable
5. Ensure all tests pass
6. Request a review from a maintainer

## Setting Up Your Development Environment

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the application:
   ```bash
   cp config.example.sh config.sh
   # Edit config.sh with your local paths and settings
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Testing

When adding new features, please consider adding tests. You can run tests with:

```bash
python -m unittest discover
```

## Documentation

Update documentation for any user-facing changes. This includes:

- Updating the README.md if necessary
- Adding JSDoc comments for any JavaScript functions
- Adding docstrings to Python functions

## Get Help

If you have questions or need help, you can:

- Open an issue with your question
- Contact the maintainers directly

## Thank You

Your contributions are what make the open-source community such a wonderful place to learn, inspire, and create. Thank you for your efforts!
