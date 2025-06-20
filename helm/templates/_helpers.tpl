{{/*
Expand the name of the chart.
*/}}
{{- define "random-jdr.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "random-jdr.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "random-jdr.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "random-jdr.labels" -}}
helm.sh/chart: {{ include "random-jdr.chart" . }}
{{ include "random-jdr.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "random-jdr.selectorLabels" -}}
app.kubernetes.io/name: {{ include "random-jdr.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "random-jdr.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "random-jdr.fullname" .) .Release.Name }}
{{- else }}
{{- default "default" .Release.Name }}
{{- end }}
{{- end }}

{{/*
-- Backend --
*/}}
{{/*
Create a default fully qualified app name for backend
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "random-jdr.backend.fullname" -}}
{{- printf "%s-%s" (include "random-jdr.fullname" .) "backend" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels for backend
*/}}
{{- define "random-jdr.backend.labels" -}}
helm.sh/chart: {{ include "random-jdr.chart" . }}
{{ include "random-jdr.backend.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels for backend
*/}}
{{- define "random-jdr.backend.selectorLabels" -}}
app.kubernetes.io/name: {{ include "random-jdr.name" . }}-backend
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the image and imagePullPolicy values for backend container based on values
*/}}
{{- define "random-jdr.backend.imageSpec" -}}
{{- $repoOwner := .Values.github.repository_owner -}}
{{- $tag := .Values.github.tag -}}
{{- $imageName := .Values.backend.image.name -}}
image: {{ printf "ghcr.io/%s/%s:%s" $repoOwner $imageName $tag | quote }}
{{- if or (contains $tag "main") (contains $tag "develop") }}
imagePullPolicy: {{ .Values.backend.image.pullPolicy | default "Always" }}
{{- else }}
imagePullPolicy: {{ .Values.backend.image.pullPolicy | default "IfNotPresent" }}
{{- end }}
{{- end }}

{{/*
-- Frontend --
*/}}
{{/*
Create a default fully qualified app name for frontend
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "random-jdr.frontend.fullname" -}}
{{- printf "%s-%s" (include "random-jdr.fullname" .) "frontend" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels for frontend
*/}}
{{- define "random-jdr.frontend.labels" -}}
helm.sh/chart: {{ include "random-jdr.chart" . }}
{{ include "random-jdr.frontend.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels for frontend
*/}}
{{- define "random-jdr.frontend.selectorLabels" -}}
app.kubernetes.io/name: {{ include "random-jdr.name" . }}-frontend
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the image and imagePullPolicy values for frontend container based on values
*/}}
{{- define "random-jdr.frontend.imageSpec" -}}
{{- $repoOwner := .Values.github.repository_owner -}}
{{- $tag := .Values.github.tag -}}
{{- $imageName := .Values.frontend.image.name -}}
image: {{ printf "ghcr.io/%s/%s:%s" $repoOwner $imageName $tag | quote }}
{{- if or (contains $tag "main") (contains $tag "develop") }}
imagePullPolicy: {{ .Values.frontend.image.pullPolicy | default "Always" }}
{{- else }}
imagePullPolicy: {{ .Values.frontend.image.pullPolicy | default "IfNotPresent" }}
{{- end }}
{{- end }}
