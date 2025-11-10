# Install timestamper plugin
node ('mac') {
  
  def exec_id = env.EXECUTOR_NUMBER : '0'
  ws("${env.workspace}@${exec_id}") {
    
    stage('build_setup') {
      sh """
        python -m pip install -r req.txt
      """
    }
    
    stage('test') {
      sh """
        pytest -q
      """
    }
    
    stage('sca') {
      sh """
        set -euxo pipefail
        ruff check .
        black --check .
        mypy src || true
      """
    }
    
    stage('Publish artifacts') {
      junit allowEmptyResults: true testResults: 'reports/junit/*.xml'
    }
  }
}
