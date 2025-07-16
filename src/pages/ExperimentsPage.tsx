import { useQuery } from '@tanstack/react-query'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

interface ExperimentSummary {
  experiment_id: string
  name: string
  run_count: number
  artifact_location: string
  lifecycle_stage: string
}

async function fetchExperiments(): Promise<ExperimentSummary[]> {
  const response = await fetch('/api/insights/experiments')
  if (!response.ok) {
    throw new Error('Failed to fetch experiments')
  }
  return response.json()
}

export function ExperimentsPage() {
  const { data: experiments, isLoading, error } = useQuery({
    queryKey: ['experiments'],
    queryFn: fetchExperiments,
  })

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-lg">Loading experiments...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-lg text-destructive">
          Error loading experiments: {error.message}
        </div>
      </div>
    )
  }

  if (!experiments || experiments.length === 0) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-lg text-muted-foreground">
          No experiments found. Start by creating an MLflow experiment.
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-semibold tracking-tight">Experiments</h2>
        <p className="text-muted-foreground">
          Overview of your MLflow experiments and their metrics
        </p>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {experiments.map((experiment) => (
          <Card key={experiment.experiment_id} className="cursor-pointer hover:shadow-md transition-shadow">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium truncate">
                {experiment.name}
              </CardTitle>
              <Badge variant={experiment.lifecycle_stage === 'active' ? 'default' : 'secondary'}>
                {experiment.lifecycle_stage}
              </Badge>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{experiment.run_count}</div>
              <p className="text-xs text-muted-foreground">
                {experiment.run_count === 1 ? 'run' : 'runs'}
              </p>
              <div className="mt-4 text-xs text-muted-foreground">
                ID: {experiment.experiment_id}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}