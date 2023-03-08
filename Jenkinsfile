pipeline{
  agent any
  stages{
    stage('version') {
      steps {
	  bat 'py --version'
	  bat 'C:\Users\MSUSERSL123\AppData\Local\Microsoft\WindowsApps\Python\pip3 install Flask'
      }
    }
    stage('hello'){
  	steps{
	  bat 'py base.py'
      }
    }
  }
}