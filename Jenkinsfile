pipeline{
  agent any
  stages{
    stage('version') {
      steps {
	  bat 'py --version'
	  bat 'pip install Flask'
      }
    }
    stage('hello'){
  	steps{
	  bat 'py base.py'
      }
    }
  }
}