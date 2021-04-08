# CS488: Computer Networks and The Internet
[Pace University](http://www.pace.edu)

Instructor: [Dr. Jun Yuan](http://csis.pace.edu/~jyuan2/)

**The content of this course changes as technology evolves**, to keep up to date with changes [follow me on GitHub](https://github.com/jyuan2pace/CS488S21).

* Section 20882. Spring 2021, Tuesday & Thursday, 12:15 PM, [Zoom meeting link](https://pace.zoom.us/j/6313313504?pwd=bUJtV3NUUlBiZVNKTThTRHBoMi84Zz09) 

# Course Description

This course provides a top-down study of modern computer networking and the Internet. Application layer topics include the Web, HTTP, FTP, SMTP, DNS, and socket programming. Transport layer topics include UDP, TCP, and congestion control. Network layer topics include link state routing, distance vector routing, IPv4, RIP, OSPF, BGP, IPv6, multicasting and IGMP, and mobile IP. Local area network topics include Ethernet, IEEE, 802.11, and Bluetooth.

# Textbook

* **[Required]**  Computer Networking: A Top-Down Approach, By James F. Kurose; Keith W. Ross. Edition: 6,  ISBN:9780132856201
* **[Recommended]** TCP/IP Illustrated, Vol. 1: The Protocols; By Richard Steves. ISBN: 978-0201633467

# Objectives

1. Understand the fundamental concepts of computer networks, particularly as related to the Internet;
2. Understand the multi-layer model of modern network architecture and its advantages and complexities;
3. Understand application layer messages and protocols, and write application layer software using sockets;
4. Understand transport layer functionality and explain how congestion control is implemented on the Internet;
5. Understand inter-networking and network layer functionality, and explain how routing is implemented on the Internet and network management;
6. Understand local area networks and link-layer issues including the details of the Ethernet and
IEEE 802.11 protocols;
7. Demonstrate your understanding of the material through a final project uploaded to GitHub.

# Syllabus
This syllabus presents the expected class schedule, due dates, and reading assignments.  [Check current syllabus.](https://docs.google.com/document/d/1xm9FhonUHEuMwYttbQLTa5kgFB2k3s4wz1XRF6_BUy4/edit?usp=sharing)

# Live Schedule
Week|Content|Recording|Reading|Quiz|Deadline
---|---|---|---|---|---
Week 1: <br>Slides [1-1](https://kami.app/p3ZfF70lkGKY) and [1-2](https://kami.app/eIjkbz8Kfdb1)<br>First class on 01/26/2021 | **Week 1: Course Intro and Logistics** <ul><li>Part 1.1: Admin and Logistics <li>Part 1.2: Internet history and overview <li>Part 1.3: Network Arch <li>Part 1.4: Design problems</ul> |<ul><li>[Logistics and overview](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4dfd3c6d-022b-422d-aa56-acbc01592d72) <li> [Network arch and layering design](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=85618b27-3616-4725-a64c-acbe015ac6f4) </ul>|<ul> <li> [Syllabus](https://docs.google.com/document/d/1xm9FhonUHEuMwYttbQLTa5kgFB2k3s4wz1XRF6_BUy4/edit?usp=sharing) <li>Chapter 1.1-1.2, 1.5, 1.7 <li>[Evolution of the TCP/IP stack(including the embeded 3min33s interview with Bob Khan)](http://som.csudh.edu/fac/lpress/471/hout/tcpiphist.htm)</ul>| Quiz#1 is out on Gradescope | Quiz#1 due 01/31/2021 
Week 2:<br>[Adds-on to week1](https://kami.app/q0LBp6YJ0VqW)<br>Week of 02/02/2021 | **Week 2: Python Prelimaries** <ul><li>	Part 2.1: Review quiz and layering <li>	Part 2.2: Packet switching <li>	Part 2.3: Network measurements <li>	Part 2.4: Variable declaration and assignment <li>Part 2.5: Integers, reals, mathematical operations on different numeric types<li>Part 2.6: Basic strings </ul> |<ul><li>[2-1 Wrapping up networking overview](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=42d11e0c-4db3-48f2-abb2-acc4008478a2) <li> [2-2. Intro to Python](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=81bd067b-8681-4bf8-81e0-acc50158366f) </ul>|<ul>Finalized reading list: <li>[Watch: How Packet Travels in Network](https://www.youtube.com/watch?v=xIuBmOufbls)<li>[Chapter 2 from Think Python](http://www.greenteapress.com/thinkpython/html/thinkpython003.html) <li>[Numbers from the Python Tutorial](https://docs.python.org/3.4/tutorial/introduction.html#numbers)<li>To be moved to next week:[Read the while and break statements from Think Python](http://www.greenteapress.com/thinkpython/html/thinkpython008.html#toc79)</ul>|Quiz#2 is on Gradescope | Quiz#2 due 02/07/2021 
Week 3:<br>[Notes](https://colab.research.google.com/drive/1DGjoeOFKo9LTWmEwVvj-Rk_FjRGxvPug?usp=sharing)<br>Week of 02/09/2021 | **Week 3: Dive into Python** <ul> <li>Part 3.1: Review IO, mathematical operations on different numeric types<li>Part 3.2: Conditions <li>Part 3.3: Loops <li>Part 3.4: Lists <li>Part 3.5: Strings </ul> |<ul><li>[3-1. Python basics](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9507e6b6-2836-453d-a99f-acca016c239e) <li> [3-2. Python basics 2](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=03505f2a-24f9-49d5-b587-accc0168c1bb) </ul>|<ul>Finalized Reading list: <li>[Read the while and break statements from Think Python](http://www.greenteapress.com/thinkpython/html/thinkpython008.html#toc79)<li>[Learn python 3 **beginner** 1-4 and 6](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#3 is out on Gradescope | Quiz#3 due 02/14/2021 
Week 4:<br>[Jam](https://jamboard.google.com/d/1t14AhwxK17gY9gHIzSBZXeXlZ6tCyo8_SlswNeAI4wE/edit?usp=sharing)<br>Week of 02/16/2021 | **Week 4: Socket Programming and WWW** <ul> <li>Part 4.1: Functions <li>Part 4.2: Socket Programming <li>Part 4.3: C/S arch <li> Part 4.4 Web server and HTTP </ul> |<ul><li>[4-1. Python wrapup and socket programming](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7ec115d0-3864-47d0-bd22-acd1016665c5) <li> [4-2. Http basics and web server](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=93d3cd9c-de11-4e71-8b3f-acd301555fe1) </ul>|<ul>Finalized Reading list: <li>Chapter 2.1-2.2, 2.7 <li>[Learn python 3 **beginner** 7 and 14](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#4 is out on Gradescope | <ul><li> Quiz#4 due 02/21/2021 <li> [Project 1](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) is out.
Week 5:<br>[Jam](https://jamboard.google.com/d/1t14AhwxK17gY9gHIzSBZXeXlZ6tCyo8_SlswNeAI4wE/edit?usp=sharing)<br>Week of 02/23/2021 | **Week 5: Build a web server** <ul> <li>Part 5.1 HTTP requests <li>Part 5.2 HTTP responses <li> 5.3 Dynamic web server <li>5.4 Web server VS. Web frame </ul> |<ul><li>[5-1. Build a web server, part 2](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=1d28b6cc-0fd8-47dc-9b46-acd8015bf13f) <li> [5-2. Build a web server, part3](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=fd96b683-0e48-43d1-a81c-acda015eb3fe) </ul>|<ul>Reading list: <li>Mininet walkthrough in your project1 document <li>[Learn python 3 **beginner** 5 and 10](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#5 is out on Gradescope | <ul><li> Quiz#5 due 02/28/2021 <li> [Project 1, milestone 1](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) is due 02/28/2021.
Week 6:<br>[Google slides](https://docs.google.com/presentation/d/1BnVbnhR7FtJYRKwTVtNGyBz5l5KELbH1oNpFQJQfB8A/edit?usp=sharing)<br>Week of 03/01/2021 | **Week 6: Intro to transport layer** <ul> <li>Part 6.1 Brainstorm: how to build an Email server <li>Part 6.2 Demultiplexing packets <li> Part 6.3 UDP <li> Part 6.4 Error detection </ul> |<ul><li>[6-1. Intro to transport layer](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=210729e9-d58c-4599-9fe6-acdf015cedab) <li> [6-2. UDP and error detection](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9a04c61b-32b3-4e93-a5b1-ace10169e28c) </ul>|<ul>Finalized reading list: <li>Chapter 3.1-3.4.1 <li>[Learn python 3 **beginner** 12 and 15](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|No quiz this week | <ul><li> Quiz#6 is paused <li> [Project 1, milestone 2](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) is due 03/07/2021.
Week 7:<br>[Google slides](https://docs.google.com/presentation/d/1FkRWBSMilS2IBqEILpv_inuri-m2uefY7e0qZhHiABw/edit?usp=sharingg) [kami](https://kami.app/Zu2YuBhkrdTW)<br>Week of 03/08/2021 | **Week 7: Reliablity** <ul> <li>Part 7.1 Reliablity basics <li>Part 7.2 Stop and wait <li>Part 7.3 Sliding window <li> Part 7.4 Congestion control  </ul> |<ul><li>[7-1. Reliablity, wait and stop](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7af11f9f-0c6c-40a1-84a3-ace60169a7f5) <li> [7-2. sliding window](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ec734e28-b026-49b7-8a6d-ace8015dc95a) </ul>|<ul>Finalized reading list: <li>Chapter 3.1-3.5.4 <li>[Learn python 3 **beginner** 12 and 15](./python_materials/learn-python3): complete the notebooks first then do exercises </ul>|Quiz#6 this week | <ul><li> Quiz#6 is resumed <li> [Project 1, milestone 3](https://docs.google.com/document/d/1LfAYkEqIO_fdRVsXhaahEP7Fjf-uOVqB5K-50kbYh60/edit?usp=sharing) is due noon 03/15/2021.
Week 8:<br>[Google slides](https://docs.google.com/presentation/d/1ng_74Z7xa--tV-4MSf36hbsgnC_smDZoiyRocAMsYW4/edit?usp=sharing) <br>Week of 03/15/2021 | **Week 8: TCP flow control and congestion control** <ul> <li>Part 8.1 Flow control and advised window <li>Part 8.2 Congestion control: program statement <li>Part 8.3 Congestion control: TCP new reno <li> Part 8.4 Wireshark on TCP header  </ul> |<ul><li>[8-1. Intro to flow control and congestion control](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bee8a6aa-5b2f-4bd6-9c07-aced0143da49) <li> [8-2. Congestion Control](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=30a0b193-e87f-45c5-bbb0-acef0140f13d) </ul>|<ul>Finalized reading list: <li>Chapter 3.5-3.8  <li>[Using wireshark to analyze a tcp packet](http://courses.washington.edu/ee461/hw/lab4.pdf). You do not need to complete the questions, just read them to prep for next week </ul>|Quiz#7 this week | <ul><li> Quiz#7 is on gradescope.  
Week 9:<br>[Google slides](https://docs.google.com/presentation/d/1b7IZkRgX9gAKnRXtvSmYZN8UAqm6n5yS7JC_kIRiO98/edit?usp=sharing) <br>Week of 03/22/2021 | **Week 9: Network layer 1: addressing and router** <ul> <li>Part 9.1 Introduction to network layer <li>Part 9.2 Internet addressing <li>Part 9.3 Router design <li> Part 9.4 Longest prefix matching  </ul> |<ul><li>[9-1. Proj2 discussion](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=98839572-74d0-4218-a026-acf4014cf40c) <li> [9-2. Network layer and IP address](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ed04dcdd-3fa4-4237-98c6-acf60142a376) </ul>|<ul>Reading list: <li>Chapter 4.1-4.4  </ul>|Quiz#8 is paused this week | <ul><li>  [Project 2: Reliability](https://docs.google.com/document/d/12CtvA1fYfuO7pB95WSkA2IR_x0ddyq2CtyLt6kgIlac/edit?usp=sharing) is out, milestone1 due 03/30
Week 10:<br>[Google slides](https://docs.google.com/presentation/d/1W_X0FtZl-VSj0BObP9N4OS3XvJuKHdfYaMtRi3VhqEw/edit?usp=sharing) <br>Week of 03/29/2021 | **Week 10: Network layer 2: IP protocol** <ul> Part 10.1 Router design <li> Part 10.2 Longest prefix matching  <li> Part 10.3 IP protocol <li> Part 10.4 Routing algorithm 1 </ul> |<ul><li>[10-1. Router design and IP match](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9e637d78-00db-4360-ae0d-acfb01406515) <li> [10-2: Network protocol, IPv4, ICMP, DHCP and NAT](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0f906d6a-d2c5-4f55-b4f2-acfd0151e90d) </ul>|<ul>Reading list: <li>Chapter 4.1-4.4  </ul>|Quiz#8 is resumed this week | <ul><li>  [Project 2 task 3 is extended to 04/08]() 
Week 11:<br>[Kami slides](https://kami.app/5UTT1axL4U2t) <br>Week of 04/06/2021 | **Week 11: Routing of the internet** <ul> Part 11.1 Intro to routing  <li> Part 11.2 Link state protocols  <li> Part 11.3 Distance vector protocols <li> Part 11.3 BGP <li> Part 11.4 Routing for the internet </ul> |<ul><li>[11-1. IPv6, ARP and Intro to routing](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=08a5212b-a8db-494a-b3b5-ad02014f28ea) <li> [11-2. Routing algorithms](https://pace.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=821a78fa-389a-46aa-bf3d-ad0401505500) </ul>|<ul>Reading list: <li>Chapter 4.44 and 4.5-4.6  </ul>|Quiz#9 this week | <ul><li>  [Project 3](https://docs.google.com/document/d/1youo4dj2EI8ng42hxoC7TlqWm5XO5hVleElCxjukfMM/edit?usp=sharing) is out, possible milestone1(proposal) due 04/14/2021
# Hands-out
* [Python 3 Cheating Sheet](./python_materials/python3cheatsheet.pdf)
* [Virtualize Python Execution](http://www.pythontutor.com/visualize.html#mode=edit)
