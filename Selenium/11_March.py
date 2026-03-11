'''
Software testing :
->Software testing is the process of evaluating a software application to ensure it works as expected and is free of defects. It helps improve quality, reliability, security, and performance before the software is released to users.

Ways:
Manual Testing:
->Performed by a human tester
->No automation tools used

Advantages:
-Better for exploratory testing  Humans can easily find UI/UX issues and unexpected bugs.
-No programming knowledge required  Testers can test without writing scripts.
-Good for small projects  Quick to start without setup.

Disadvantages:
-Time-consuming  Repeating the same tests manually takes a lot of time.
-Human errors  Testers may miss some bugs.
-Not suitable for large or repetitive testing.



Automated Testing:
->Uses tools and scripts
->Faster and suitable for repetitive tasks

Advantages:
Fast execution Tests run much faster than manual testing.
Reusable test scripts Once written, scripts can be reused many times.
Better for large and repetitive testing (like regression testing).

Disadvantages:
High initial setup cost Tools and script development take time.
Requires programming knowledge.
Not ideal for UI or exploratory testing where human observation is needed.

Selenium:
->selenium developed by Jason Huggins in 2004
->selenium is a antidote to mercury (QTC)
Selenium is an open-source framework for automating web browsers. It lets you control a browser programmatically — clicking buttons, filling forms, navigating pages, and scraping content — just as a human user would.
It's primarily used for:
Automated testing of web applications
Web scraping (extracting data from websites)
Browser automation (repetitive tasks)


components of Selenium:
-Selenium rc ( its a complex setup , cuz rc server should be seperatly setup)
-Selenium IDE(its an record and playback tool) 
-Selenium webdriver(we can't do parallel executions )
-Selenium grid (this overcomes the drawback of webdriver)(it follow hub architecture)


'''