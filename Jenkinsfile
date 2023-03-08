pipeline{
  agent { docker { image 'python:3.10.10' } }
  stages{
    stage('version') {
      steps {
	  sh 'python3 --version'
      }
    }
    stage('hello'){
  	steps{
	  sh 'python3 base.py'
      }
    }
  }
}