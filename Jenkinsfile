pipeline {

 agent any

 stages {
   stage('Checkout') {
      steps {
         checkout scm
      }
   }

   stage('Install') {
      steps {
         bat 'python -m pip install -r requirements.txt'
      }
   }

   stage('Run Tests') {
      steps {
         bat 'pytest --alluredir=allure-results'
      }
   }
 }

 post {
   always {
      allure([
      includeProperties:false,
      jdk:'',
      results:[[path:'allure-results']]
      ])
   }
 }
}
