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

Pay attention to the output, simiar to:
```
Key                 HelloWorldApi
Description         API Gateway endpoint URL for Prod stage for Hello World function, use with 'curl'
Value               https://lfu23lvlo1.execute-api.ap-southeast-2.amazonaws.com/Prod/hello/

Key                 HelloWorldFunctionName
Description         add 'aws logs tail /aws/lambda/' before the function name to see its logs
Value               sam-app-HelloWorldFunction-II22CFRfh2D2
```

You should trigger execution by invoking the `HelloWorldApi` URL

Try to make the solution fully traced by XRay. As a tiny help, this stack also deploys aws-xray-sdk libraries as a lambda layer to your account
