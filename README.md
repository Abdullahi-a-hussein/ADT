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
   This file also contains a child class <b> PriorityQueue</b>, of the Queue class. The only difference is how items are added to the queue. PriorityQueue addes     items to the queue using the give priority instructions. Just like, people with disability are given priority in a queue of people for some sort of services.
  <li><a href="https://github.com/Abdullahi-a-hussein/ADT/blob/master/Linkedlist/linkedlist.py">Linked list</a> </li>
  <p> This file contains implementation code for ADT singly linked list. The class <b>_node</b> is used to constract an item in this linked list. Any element of this linked list is either none, or it has tow elements: an item that holds the value of this node and a pointer that point towards the next item of the list.</p>
  
  <p> The follwing are some of the methods of this class:
   <ul>
      <li> Append </li>
      <p> This addes new item at the end of the linked list </p>
      <li> insert </li>
      <p> This inserts the given item at the specified position of this linked list.</p>
      <li> len <li>
      <p> This returns the number of items in this linked list. </p>
      <li> getitem </li>
      <p>This returns the value stored at the provided index. </p>
      <li>setitem </li>
      <p> This changes the value stored at the given index to the new provided value. <p>
      <li> contains <li>
      <p> This checks wether the provided item is in this linked list and returns false if it is not and True if it is </p>
      <li> reverse </li>
      <p> This reverses the order of the elements in this linked list. The first elemetn in this linked list becomes the last element. </p>
      <li> count </li>
      <p> This returns the number of times the provided item occurs in this linked list.</p>
      <li> pop </li>
      <p> This method removes and returns the last item of this linked list.</p>
      <li> extend </li>
      <p> This concatinates the given linked list to this linked list to form single linked list.</p>
      <li> Remove <li>
      <p> Removes the first occurance of the provided item. It raised IndexError if Item is not in this linked list.</p>
   </ul>
</ul>
