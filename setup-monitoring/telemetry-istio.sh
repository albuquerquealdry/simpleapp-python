echo "[DOWLOAND ISTIO]"
echo "=================================="
curl -L https://istio.io/downloadIstio | sh -
echo "[INSTALL ISTIO]"
echo "=================================="
istio-1.15.1/bin/istioctl install --set profile=demo -y
echo "[LABEL NAMESPACE]"
echo "=================================="
kubectl label namespace default istio-injection=enabled
kubectl delete pods --all -n default
echo "[INSTALL STACK TELEMETRY && OBSERVABILITY]"
echo "=================================="
kubectl apply -f istio-1.15.1/samples/addons