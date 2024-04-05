from azureml.core.model import InferenceConfig
from azureml.core import Model, Environment

# Create an environment for the deployment
env = Environment(name="myenv")
env.python.conda_dependencies.add_pip_package("numpy")
env.python.conda_dependencies.add_pip_package("scikit-learn")
env.python.conda_dependencies.add_pip_package("joblib")

# Configure the scoring script and environment for inference
inference_config = InferenceConfig(entry_script="scoring.py", environment=env)

# Get the registered model
model = Model(workspace=ws, name="gradient")

# Deploy the model as a web service
service = Model.deploy(
    workspace=ws,
    name="myservice",
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
)

service.wait_for_deployment(show_output=True)
