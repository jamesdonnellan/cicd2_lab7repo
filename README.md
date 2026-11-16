# Lab 7 CICD2 - Using RabbitMQ

# What is the difference between a producer, a queue and a consumer?
- Producer sends messages.
- Queue stores messages.
- Consumer receives and processes messages.

# When the worker was stopped, why did the Ready count increase? 
- Messages were being published but no consumer was available to process them.

# What changed in RabbitMQ Management while the worker was processing a message? 
- Consumers became 1.
- Unacknowledged became 1.
- Ready decreased.

# What does HTTP 202 Accepted tell the client, and what does it not guarantee? 
- The request was accepted for processing.
- It does not guarantee the work has completed successfully.

# Why is await useful when a FastAPI endpoint communicates with RabbitMQ? 
- The FastAPI endpoint can wait for RabbitMQ without blocking the event loop.

# What changed when you set prefetch_count=2? Did the worker actually process two orders at the same time? 
- RabbitMQ could send two unacknowledged messages to the worker.
- The worker still processed them one at a time.

# With two consumers using prefetch_count=1, what did the Consumers and Unacknowledged counts show? 
- 2

# What happened when one worker stopped before acknowledging an order? Why can the same message be delivered twice? 
- RabbitMQ requeued the message and another consumer could receive it.

# In your own words, what does an event loop do while an async function is awaiting a network operation? 
- When an async function is waiting for something from the network, the event loop switches to other tasks instead of waiting around. When the response arrives, it goes back and continues where it left off.