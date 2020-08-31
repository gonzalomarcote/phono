### Create secrets needed for MQTT broker

Encode your ssl certs with base64:

    base64 -w0 broker/config/ca_certificates/chain.pem
    base64 -w0 broker/config/certs/cert.pem
    base64 -w0 broker/config/certs/privkey.pem

Create a ssl secret file `ca-secret.yaml` for ca:

```
apiVersion: v1
data:
  chain.pem: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2QUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktZd2dnU2lBZ0VBQW9JQkFRQ1lrL2hMaEMzalh2Y3kKUHY1VDdNcU1OMWR5STlQNVM5MlpUUllNT1VZb2JiUXREeE1KbWxMd3g4c0owQURlWjVzTWRSQkYwWjJzNVBrMApHL3V2d2c2c2JpSTFCaXVqaVBzdnRwWVpIaC9nZVdJUG5zS....
kind: Secret
metadata:
  name: ca-secret
type: Opaque
```

And create a ssl secret file `certs-secret.yaml` for certs:
```
apiVersion: v1
data:
  cert.pem: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2QUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktZd2dnU2lBZ0VBQW9JQkFRQ1lrL2hMaEMzalh2Y3kKUHY1VDdNcU1OMWR5STlQNVM5MlpUUllNT1VZb2JiUXREeE1KbWxMd3g4c0owQURlWjVzTWRSQkYwWjJzNVBrMApHL3V2d2c2c2JpSTFCaXVqaVBzdnRwWVpIaC9nZVdJUG5zS....
  privkey.pem: S0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURHRENDQWdBQ0NRRHJDajdxWHFhR1VqQU5CZ2txaGtpRzl3MEJBUXN….
kind: Secret
metadata:
  name: certs-secret
type: Opaque
```

Create the secret:

    $ kubectl apply -f ca-secret.yaml -n phono-dev -n phono-release -n phono
    $ kubectl apply -f certs-secret.yaml -n phono-dev -n phono-release -n phono


Mount secrets in the broker deployment:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  ...
    spec:
      restartPolicy: Always
      containers:
      - name: {{ .Values.deployment.containerName }}
        image: {{ .Values.deployment.image }}:{{ .Values.deployment.tag }}
        imagePullPolicy: {{ .Values.deployment.pullPolicy }}
        ports:
        - containerPort: {{ .Values.deployment.containerPort }}
          name: {{ .Values.deployment.containerPortName }}
        - containerPort: {{ .Values.deployment.containerPortTLS }}
          name: {{ .Values.deployment.containerPortNameTLS }}
        volumeMounts:
        - name: {{ .Values.deployment.volumeMountsName }}
          mountPath: {{ .Values.deployment.volumeMountsMountPath }}
        - name: ca-secret
          mountPath: "/mqtt/config/ca_certificates/"
          readOnly: true
        - name: certs-secret
          mountPath: "/mqtt/config/certs/"
          readOnly: true
      volumes:
      - name: {{ .Values.deployment.volumesName }}
        persistentVolumeClaim:
          claimName: {{ .Values.deployment.volumesClaimName }}
      - name: ca-secret
        secret:
          secretName: ca-secret
      - name: certs-secret
        secret:
          secretName: certs-secret
      imagePullSecrets:
      - name: {{ .Values.deployment.imagePullSecrets }}
```
