# Kipesa Chatbot Implementation

## Overview

The Kipesa chatbot is an AI-powered financial assistant designed specifically for Tanzanian users. It provides personalized financial advice, helps with budgeting, explains Tanzanian financial regulations, and assists with financial planning in both English and Swahili.

## Features

### 🤖 Core Chatbot Features
- **Multi-language Support**: English and Swahili
- **Conversation Management**: Track conversation history and context
- **Personalization**: User profile-based responses
- **Knowledge Integration**: Tanzanian financial regulations and best practices
- **Intent Classification**: Automatic understanding of user queries
- **Entity Extraction**: Extract financial amounts, time periods, etc.
- **Sentiment Analysis**: Track user satisfaction

### 📊 Analytics & Monitoring
- **Performance Metrics**: Response times, confidence scores
- **Usage Analytics**: Conversation counts, language distribution
- **Intent Tracking**: Most common user queries
- **Feedback System**: User ratings and feedback collection

### 🔧 Technical Features
- **Async Processing**: Non-blocking message handling
- **Caching**: Knowledge base and conversation caching
- **Error Handling**: Comprehensive error management
- **Rate Limiting**: API rate limiting for stability
- **Logging**: Detailed logging for monitoring

## Architecture

### Database Schema

#### Core Tables
- `conversations`: Store conversation metadata
- `chat_messages`: Store individual messages
- `chatbot_analytics`: Store analytics data
- `chatbot_feedback`: Store user feedback
- `knowledge_base`: Store financial knowledge content

#### Relationships
```
conversations (1) -> (many) chat_messages
conversations (1) -> (many) chatbot_analytics
chat_messages (1) -> (many) chatbot_feedback
```

### Service Layer

#### ChatbotService
- **create_conversation()**: Start new conversations
- **process_message()**: Handle user messages
- **get_conversation_history()**: Retrieve conversation history
- **submit_feedback()**: Handle user feedback
- **get_analytics()**: Generate analytics reports

#### Key Methods
- `_generate_response()`: OpenAI API integration
- `_get_relevant_knowledge()`: Knowledge base search
- `_analyze_response()`: Intent and sentiment analysis
- `_classify_intent()`: Intent classification
- `_extract_entities()`: Entity extraction

## API Endpoints

### Core Chatbot Endpoints

#### POST `/chatbot/conversation`
Start a new conversation.

**Request:**
```json
{
  "initial_message": "Hello, I need help with budgeting",
  "language": "en",
  "user_id": 123,
  "context": {"source": "web"}
}
```

**Response:**
```json
{
  "conversation_id": "uuid",
  "messages": [...],
  "language": "en",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z",
  "user_id": 123,
  "metadata": {...}
}
```

#### POST `/chatbot/chat`
Send a message and get a response.

**Request:**
```json
{
  "message": "How much should I save each month?",
  "conversation_id": "uuid",
  "language": "en",
  "user_id": 123,
  "context": {...}
}
```

**Response:**
```json
{
  "conversation_id": "uuid",
  "message": "Based on your income...",
  "language": "en",
  "confidence": 0.85,
  "intent": "savings_advice",
  "entities": [...],
  "sentiment": "positive",
  "response_time": 1.23,
  "metadata": {...}
}
```

#### GET `/chatbot/conversation/{conversation_id}`
Get conversation history.

#### POST `/chatbot/feedback`
Submit feedback for a response.

#### GET `/chatbot/analytics`
Get chatbot analytics.

#### GET `/chatbot/health`
Check chatbot service health.

#### GET `/chatbot/languages`
Get supported languages.

#### GET `/chatbot/intents`
Get supported intents.

## Configuration

### Environment Variables

```bash
# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=500
OPENAI_TEMPERATURE=0.7

# Chatbot Configuration
CHATBOT_CACHE_TTL=3600
CHATBOT_MAX_HISTORY=10
CHATBOT_RESPONSE_TIMEOUT=30

# Redis Configuration (for caching)
REDIS_URL=redis://localhost:6379
REDIS_DB=0
```

### Database Setup

Run the migration to create chatbot tables:

```sql
-- Run the migration file: app/db/migrations/003_create_chatbot_tables.sql
```

## Usage Examples

### Python Client Example

```python
import asyncio
from app.services.chatbot import chatbot_service
from app.schemas.chatbot import ChatRequest, Language

async def chat_example():
    async with AsyncSessionLocal() as db:
        # Send a message
        request = ChatRequest(
            message="I need help with my budget",
            language=Language.ENGLISH
        )
        
        response = await chatbot_service.process_message(db, request)
        print(f"Response: {response.message}")
        print(f"Intent: {response.intent}")
        print(f"Confidence: {response.confidence}")
```

### cURL Examples

#### Start a conversation:
```bash
curl -X POST "http://localhost:8000/chatbot/conversation" \
  -H "Content-Type: application/json" \
  -d '{
    "initial_message": "Hello, I need financial advice",
    "language": "en"
  }'
```

#### Send a message:
```bash
curl -X POST "http://localhost:8000/chatbot/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "How much should I save each month?",
    "conversation_id": "your-conversation-id",
    "language": "en"
  }'
```

## Knowledge Base

### Content Categories
- **Regulations**: Bank of Tanzania, TRA regulations
- **Practices**: Financial best practices
- **FAQ**: Common financial questions

### Sources
- Bank of Tanzania (BoT)
- Tanzania Revenue Authority (TRA)
- Financial education materials

### Adding Knowledge

To add new knowledge base content:

```sql
INSERT INTO knowledge_base (id, title, content, category, language, source) VALUES (
    'kb-006',
    'New Financial Topic',
    'Content about the new topic...',
    'practice',
    'en',
    'Source Name'
);
```

## Intent Classification

### Supported Intents
- `budget_help`: Budgeting and expense management
- `savings_advice`: Saving money and investments
- `loan_advice`: Loans and credit
- `tax_help`: Tax-related questions
- `regulation_info`: Financial regulations
- `greeting`: General greetings
- `general_help`: General financial advice

### Entity Extraction

The chatbot extracts:
- **Amounts**: Currency values (TSh, USD, etc.)
- **Time Periods**: Months, years, weeks
- **Financial Terms**: Budget, savings, loans, etc.

## Performance Optimization

### Caching Strategy
- **Knowledge Base**: Cache frequently accessed content
- **Conversation History**: Cache recent conversations
- **User Profiles**: Cache user preferences

### Response Time Optimization
- **Async Processing**: Non-blocking API calls
- **Connection Pooling**: Database connection optimization
- **Caching**: Reduce redundant API calls

## Monitoring & Analytics

### Key Metrics
- **Response Time**: Average response time
- **Confidence Score**: AI response confidence
- **User Satisfaction**: Feedback ratings
- **Intent Distribution**: Most common user intents
- **Language Usage**: English vs Swahili usage

### Logging
- **Request Logging**: All incoming requests
- **Error Logging**: Detailed error information
- **Performance Logging**: Response times and bottlenecks

## Testing

### Running Tests

```bash
# Run the test script
cd backend
python test_chatbot.py
```

### Test Coverage
- Conversation creation and management
- Message processing and response generation
- Multi-language support (English/Swahili)
- Analytics and feedback systems
- Error handling and edge cases

## Security Considerations

### Authentication
- JWT token-based authentication
- User-specific conversation isolation
- Rate limiting to prevent abuse

### Data Privacy
- User data encryption
- Conversation history retention policies
- GDPR compliance considerations

### API Security
- Input validation and sanitization
- SQL injection prevention
- CORS configuration

## Deployment

### Requirements
- Python 3.8+
- PostgreSQL database
- Redis (optional, for caching)
- OpenAI API access

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export OPENAI_API_KEY="your-api-key"

# Run database migrations
# (Execute the SQL migration file)

# Start the server
python -m uvicorn app.main:app --reload
```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Troubleshooting

### Common Issues

#### OpenAI API Errors
- Check API key configuration
- Verify API quota and limits
- Check network connectivity

#### Database Connection Issues
- Verify database URL configuration
- Check database server status
- Ensure proper table creation

#### Performance Issues
- Monitor response times
- Check OpenAI API latency
- Review caching configuration

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Future Enhancements

### Planned Features
- **Advanced NLP**: Better intent classification
- **Voice Support**: Speech-to-text integration
- **Multi-modal**: Image and document analysis
- **Advanced Analytics**: Machine learning insights
- **Integration**: Third-party financial APIs

### Scalability Improvements
- **Microservices**: Separate chatbot service
- **Load Balancing**: Multiple chatbot instances
- **Advanced Caching**: Redis cluster setup
- **Monitoring**: Prometheus/Grafana integration

## Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Implement changes with tests
4. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Add comprehensive tests
- Update documentation
- Include type hints

## License

This chatbot implementation is part of the Kipesa financial platform and follows the same licensing terms.

---

For more information, contact the development team or refer to the main project documentation. 