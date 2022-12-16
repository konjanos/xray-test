# xray-test
Sample Lambda function prepared to be traced by x-ray

Deploy it by starting a CloudShell console (which has all the tools installed and will use your credentials, so you're good to go):
```
# git clone https://github.com/konjanos/xray-test.git
# cd xray-test
# sam build
# sam validate
# sam deploy --guided
```

You can mostly go with the defaults except for:
> HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y

Use the `main` branch to start with, try to make the solution fully traced by XRay. As a tiny help, this stack also deploys aws-xray-sdk libraries as a lambda layer to your account

In case you stuck, you can deploy `traced` branch, which has full tracing configured.
