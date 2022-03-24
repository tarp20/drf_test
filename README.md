# drf_test

Simple MVP. It will have a list of news with functionality to upvote and comment on them. Similar platform to HackerNews.

## **Functional Requirements**

- Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name
- Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date
- There should be an endpoint to upvote the post
- We should have a recurring job running once a day to reset post upvotes count



## **Brief description**

The projects works on PostgreSQL using psycopg2 library at Python site. 


### **Steps to start on**

You can move right through the steps to start the project on your computer, or just use Docker container (next chapter).    
`docker-compose up`


 Download the project from github    
`git pull https://github.com/tarp20/drf_test`

run docker build .
after docker-compose up  
  

## **Postman**

unfortunately I have no experience in creating postman documentation , but but everything is tested and in a short time I will figure out it.
## **Deploy**
[Deploy on Heroku link](https://tarnews.herokuapp.com)
