pipeline{
  agent any
  stages{
    stage('version') {
      steps {
	  bat 'py --version'
	  bat 'py -3 -mpip install Flask'
      }
    }
    stage('hello'){
  	steps{
	  bat 'py base.py'
      }
    }
  }
}