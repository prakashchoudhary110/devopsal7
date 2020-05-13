FROM centos:latest

RUN yum install wget -y
RUN yum install net-tools -y
RUN wget -D /etc/yum.repos.d/jenkins.repo http://pkg.jenkins.io/redhat/jenkins.repo
RUN rpm --import http://pkg.jenkins.io/redhat/jenkins.io.key
RUN yum install java -y
RUN yum install jenkins -y
RUN yum install git -y
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN yum insatll python3 -y
RUN mail.py /

CMD java -jar /usr/lib/jenkins/jenkins.war
