# GitHub Copilot Instructions - S (Telegram Bot)

## Project Overview
This is a simple Telegram bot built using the aiogram framework (version 3.13.1). The bot responds to commands and messages, providing basic echo and acknowledgment functionality.

## Language & Framework
- **Language**: Python 3.x
- **Main Framework**: aiogram 3.13.1
- **Async Framework**: asyncio

## Coding Standards

### Python Style
- Follow PEP 8 coding standards
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use type hints where applicable
- Use async/await for all bot handlers and async operations

### Naming Conventions
- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private methods/variables: prefix with single underscore `_private_method`

### Import Organization
```python
# Standard library imports
import asyncio
import logging
import os

# Third-party imports
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
```

## Framework-Specific Guidelines

### aiogram Best Practices
- Use filters (CommandStart, Command, F) for message handling
- Always use `async def` for handlers
- Use dependency injection for bot and dispatcher instances
- Use proper type hints with aiogram types (Message, CallbackQuery, etc.)
- Handle errors gracefully with try-except blocks

### Bot Handlers
- Name handler functions descriptively: `on_start`, `on_echo`, `on_text`
- Register handlers using decorators: `@dp.message()`
- Use proper filters to match specific message types
- Always await async operations

## Security Practices

### Environment Variables
- **NEVER** hardcode bot tokens or sensitive data
- Always use environment variables for secrets
- Store tokens in `.env` file (which is gitignored)
- Validate that required environment variables are set before running
- Use `os.getenv()` with proper defaults or error handling

### Input Validation
- Validate all user inputs before processing
- Sanitize user-provided text before using in responses
- Be cautious with file uploads and external URLs
- Implement rate limiting for bot commands if needed

### Error Handling
- Always wrap bot operations in try-except blocks
- Log errors properly using Python's logging module
- Don't expose sensitive information in error messages to users
- Handle bot API errors gracefully

## Testing Guidelines

### General Testing Approach
- Write unit tests for business logic
- Use pytest for testing Python code
- Mock external dependencies (Telegram API calls)
- Test error handling paths
- Aim for high test coverage of critical paths

### Bot Testing
- Mock aiogram Bot and Dispatcher for testing
- Test handler functions independently
- Verify correct responses for different commands
- Test edge cases (empty messages, long messages, etc.)

## Documentation Standards

### Code Documentation
- Add docstrings to all functions and classes
- Use clear, descriptive function and variable names
- Document complex logic with inline comments
- Keep comments up-to-date with code changes

### Docstring Format
```python
async def on_echo(message: Message):
    """
    Handle /echo command to repeat user's message.
    
    Args:
        message: The incoming message object from Telegram
        
    Returns:
        None (sends reply to user)
    """
```

### README Updates
- Update README.md when adding new commands or features
- Keep installation and usage instructions current
- Document all environment variables
- Include examples for new functionality

## Dependencies

### Adding New Dependencies
- Only add dependencies when absolutely necessary
- Specify exact versions in requirements.txt
- Document why each dependency is needed
- Check for security vulnerabilities before adding

### Current Dependencies
- aiogram==3.13.1 (Telegram Bot framework)

## Build & Run

### Development Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add BOT_TOKEN

# Run bot
python quickstart_bot.py
```

### Running Tests
```bash
# Run tests with pytest
pytest

# Run with coverage
pytest --cov
```

## Git Workflow

### Commits
- Write clear, descriptive commit messages
- Use present tense ("Add feature" not "Added feature")
- Keep commits focused and atomic
- Reference issue numbers when applicable

### Files to Ignore
- Never commit `.env` files
- Ignore `__pycache__/` and `*.pyc` files
- Ignore IDE-specific files (`.vscode/`, `.idea/`)
- Ignore virtual environments (`venv/`, `env/`)

## Internationalization
- The bot currently uses Thai language for user-facing messages
- Keep Thai messages consistent and natural
- Use UTF-8 encoding for all files
- Consider adding English translations for broader audience

## Error Messages & Logging

### Logging
- Use Python's `logging` module, not print statements
- Set appropriate log levels (INFO, WARNING, ERROR)
- Include context in log messages
- Format: `"%(asctime)s %(levelname)s %(message)s"`

### User-Facing Messages
- Keep error messages friendly and helpful
- Guide users on how to fix issues
- Use emojis appropriately (✅ for success, ❌ for errors)
- Provide clear instructions for next steps

## Performance Considerations
- Use async/await properly to avoid blocking operations
- Keep handler functions lightweight and fast
- Consider rate limiting for resource-intensive operations
- Monitor bot performance and response times

## Common Tasks

### Adding a New Command
1. Create an async handler function
2. Register it with `@dp.message(Command("command_name"))`
3. Implement the logic
4. Update README.md with the new command
5. Add tests for the new command

### Modifying Bot Responses
- Keep responses consistent with existing style
- Use proper Thai grammar and phrasing
- Test responses for different input scenarios
- Ensure responses are helpful and clear
