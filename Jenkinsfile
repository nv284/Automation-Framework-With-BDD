pipeline {

 agent any

 stages {

   stage('Install') {
      steps {
         bat 'pip install -r requirements.txt'
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
