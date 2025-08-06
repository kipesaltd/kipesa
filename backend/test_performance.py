#!/usr/bin/env python3
"""
Performance testing script for Kipesa application.
"""

import asyncio
import time
import aiohttp
import json
from typing import List, Dict, Any
from loguru import logger

class PerformanceTester:
    """Performance testing for the Kipesa API."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.results = []
    
    async def test_chatbot_response_time(self, message: str, language: str = "en") -> Dict[str, Any]:
        """Test chatbot response time."""
        start_time = time.time()
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "message": message,
                    "language": language,
                    "context": {"test": True}
                }
                
                async with session.post(
                    f"{self.base_url}/chatbot/chat",
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    end_time = time.time()
                    response_time = end_time - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        return {
                            "success": True,
                            "response_time": response_time,
                            "message_length": len(data.get("message", "")),
                            "status_code": response.status
                        }
                    else:
                        return {
                            "success": False,
                            "response_time": response_time,
                            "status_code": response.status,
                            "error": await response.text()
                        }
                        
        except Exception as e:
            end_time = time.time()
            return {
                "success": False,
                "response_time": end_time - start_time,
                "error": str(e)
            }
    
    async def test_conversation_creation(self, message: str, language: str = "en") -> Dict[str, Any]:
        """Test conversation creation time."""
        start_time = time.time()
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "initial_message": message,
                    "language": language,
                    "context": {"test": True}
                }
                
                async with session.post(
                    f"{self.base_url}/chatbot/conversation",
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    end_time = time.time()
                    response_time = end_time - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        return {
                            "success": True,
                            "response_time": response_time,
                            "conversation_id": data.get("conversation_id"),
                            "status_code": response.status
                        }
                    else:
                        return {
                            "success": False,
                            "response_time": response_time,
                            "status_code": response.status,
                            "error": await response.text()
                        }
                        
        except Exception as e:
            end_time = time.time()
            return {
                "success": False,
                "response_time": end_time - start_time,
                "error": str(e)
            }
    
    async def run_performance_test(self, num_requests: int = 10) -> Dict[str, Any]:
        """Run comprehensive performance test."""
        logger.info(f"Starting performance test with {num_requests} requests...")
        
        test_messages = [
            "Help me create a budget for my monthly expenses",
            "What are the best investment options in Tanzania?",
            "Explain the different types of bank accounts",
            "How can I save money effectively?",
            "What are the tax requirements for small businesses?"
        ]
        
        results = {
            "chatbot_responses": [],
            "conversation_creation": [],
            "summary": {}
        }
        
        # Test chatbot responses
        for i in range(num_requests):
            message = test_messages[i % len(test_messages)]
            result = await self.test_chatbot_response_time(message)
            results["chatbot_responses"].append(result)
            logger.info(f"Chatbot test {i+1}/{num_requests}: {result['response_time']:.2f}s")
        
        # Test conversation creation
        for i in range(num_requests):
            message = test_messages[i % len(test_messages)]
            result = await self.test_conversation_creation(message)
            results["conversation_creation"].append(result)
            logger.info(f"Conversation test {i+1}/{num_requests}: {result['response_time']:.2f}s")
        
        # Calculate summary statistics
        successful_chatbot = [r for r in results["chatbot_responses"] if r["success"]]
        successful_conversations = [r for r in results["conversation_creation"] if r["success"]]
        
        if successful_chatbot:
            chatbot_times = [r["response_time"] for r in successful_chatbot]
            results["summary"]["chatbot"] = {
                "avg_response_time": sum(chatbot_times) / len(chatbot_times),
                "min_response_time": min(chatbot_times),
                "max_response_time": max(chatbot_times),
                "success_rate": len(successful_chatbot) / len(results["chatbot_responses"])
            }
        
        if successful_conversations:
            conversation_times = [r["response_time"] for r in successful_conversations]
            results["summary"]["conversation"] = {
                "avg_response_time": sum(conversation_times) / len(conversation_times),
                "min_response_time": min(conversation_times),
                "max_response_time": max(conversation_times),
                "success_rate": len(successful_conversations) / len(results["conversation_creation"])
            }
        
        return results

async def main():
    """Main performance test function."""
    tester = PerformanceTester()
    
    # Run performance test
    results = await tester.run_performance_test(num_requests=20)
    
    # Print results
    print("\n" + "="*50)
    print("PERFORMANCE TEST RESULTS")
    print("="*50)
    
    if "chatbot" in results["summary"]:
        chatbot = results["summary"]["chatbot"]
        print(f"\nChatbot Response Times:")
        print(f"  Average: {chatbot['avg_response_time']:.2f}s")
        print(f"  Min: {chatbot['min_response_time']:.2f}s")
        print(f"  Max: {chatbot['max_response_time']:.2f}s")
        print(f"  Success Rate: {chatbot['success_rate']:.1%}")
    
    if "conversation" in results["summary"]:
        conversation = results["summary"]["conversation"]
        print(f"\nConversation Creation Times:")
        print(f"  Average: {conversation['avg_response_time']:.2f}s")
        print(f"  Min: {conversation['min_response_time']:.2f}s")
        print(f"  Max: {conversation['max_response_time']:.2f}s")
        print(f"  Success Rate: {conversation['success_rate']:.1%}")
    
    # Performance recommendations
    print(f"\nPerformance Recommendations:")
    if "chatbot" in results["summary"]:
        avg_time = results["summary"]["chatbot"]["avg_response_time"]
        if avg_time > 5.0:
            print("  ⚠️  Chatbot responses are slow (>5s). Consider:")
            print("     - Implementing caching")
            print("     - Optimizing OpenAI API calls")
            print("     - Using connection pooling")
        elif avg_time > 3.0:
            print("  ⚠️  Chatbot responses are moderate (3-5s). Consider:")
            print("     - Adding Redis caching")
            print("     - Optimizing database queries")
        else:
            print("  ✅ Chatbot responses are fast (<3s)")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    asyncio.run(main()) 