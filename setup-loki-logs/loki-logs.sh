echo "[GET CHART LOKI]"
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
echo "[Install Loki]"
kubectl create ns loki
helm install logs grafana/loki-stack --namespace loki --create-namespace --set grafana.enabled=true
kubectl patch svc logs-grafana -n loki  -p '{"spec": {"type": "LoadBalancer"}}'
echo "[Your Credential]"
kubectl get secret --namespace loki logs-grafana  -o jsonpath="{.data.admin-password}" | base64 --decode ; echo