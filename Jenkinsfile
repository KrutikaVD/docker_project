pipeline{
  agent any
  stages{
    stage('version') {
      steps {
	  bat 'py --version'
	  bat 'py -3 -mpip install Flask'
	  bat 'py -3 -mpip install flask_restful'
      }
    }
    stage('hello'){
  	steps{
	  bat 'py base.py'
      }
    }
  }
}