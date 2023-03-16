# My-Calculator

A simple calculator.

My second Python project!

The first of four 'simple' projects for my Python portfolio.

Following the advice of Andy Sterkowitz, my simple project would use the basic Python library; use less than 200 lines of code; use the CLI as opposed to GUI or WebApp.

What does it do?

I  modeled my project on the Window's calculator, with features such as stored input and memory. Using the CLI, the user can input operands and operators, store these and perform operations. The actual operations are performed by the eval() function, which translates all parts of the array into bytecode, peforms the calculation and returns an integer. Before (re-)discovering eval(), I tried unsuccessfully to achieve something similar using bin(). I preferred using eval() as it dealt with order of operations (BIDMAS) for me. Using the os module from the Python standard library I improved the user's experience by clearing the CLI for every new input so the interface did not become unsightly. 

What doesn't it do?

By definition, the scope of a simple project is limited. As I am using the CLI, the user's interface is not pretty. As with my first project, no unit testing was performed but using a calculator is quite intuitive. I did implement some try-except blocks where they related to the internal functioning of the program. 

What went wrong the first time?

I made two attempts at this project. On the first attempt I made my program too complex in that I did not understand how the classes related, the meaning of the variables and that I was dealing with a mix of datatypes. The latter issue was my greatest problem, it was caused by trying to using the eval() function too early into the program's procedure. On my second attempt, I sketched out in my notepad the different classes I planned to create, their relation to each other and what datatypes would be used. I limited used of the eval() function to expressions relating directly to things that were to be shown to the user by outputting them. Otherwise, the operands and operators were stored in lists. Simplifying things down to only two data types helped greatly as I could then focus on the more abstracts parts of the program as opposed to modifying data types.