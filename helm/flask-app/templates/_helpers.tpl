{{- define "flask-app.name" -}}
{{- .Chart.Name -}}
{{- end }}

{{- define "flask-app.fullname" -}}
{{- .Release.Name -}}
{{- end }}

{{- define "flask-app.labels" -}}
app.kubernetes.io/name: {{ include "flask-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}