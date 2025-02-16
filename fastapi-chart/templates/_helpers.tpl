{{- define "dns-api.name" -}}
{{ .Release.Name }}-dns-api
{{- end }}

{{- define "dns-api.labels" -}}
app: {{ .Release.Name }}-dns-api
{{- end }}
