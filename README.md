# Abstract Data Types (ADT)
This repo contains implementation of various Abstract Data types.  The language I use is Python 3. The following are included ADT to date:

<ul> 
   <li> <h2><a href="https://github.com/Abdullahi-a-hussein/ADT/blob/master/Stack/stack.py"> Stack</a> </h2></li>
   <p> This contains <b> LIFO </b> ADT with the following basic operational methods. 
   <ul>
      <li> Push method </li>
      <p> This appends new elements to the stack </p>
      <li> Pull method </li>
      <p> This removes and prints the top most item of the stack </p>
   </ul>
   This file also contains a <b>GuardedStack</b> child class of <b> stack </b> where new stack elements is added to the stack if they pass the guard.
   </p>
   <li cols="gree"> <h2><a href="https://github.com/Abdullahi-a-hussein/ADT/blob/master/Queue/queue.py"> Queue </a> </h2></li>
    <p> This file contains implementation code for <b>FIFO</b> ADT with the following basic methods. </p>
    <ul>
   <li>enqueue </li>
   <p> This addes new items at the end of the queue </p>
   <li>dequeue </li>
   This removes and returns the first item that was added to the queue out of the remaining items in the queue. 
   </ul>
   This file also contains a child class <b> PriorityQueue</b>, of the Queue class. The only difference is how items are added to the queue. PriorityQueue addes items to the queue using the give priority instructions. Just like, people with disability are given priority in a queue of people for some sort of services.
</ul>
