__author__ = 'cjoakim'

from .distance import Distance
from .elapsed_time import ElapsedTime
from .speed import Speed


class RunWalkCalculator(object):

    @classmethod
    def calculate(cls, run_hhmmss, run_ppm, walk_hhmmss, walk_ppm, miles):
        result = dict()
        result['run_hhmmss'] = run_hhmmss
        result['run_ppm'] = run_ppm
        result['walk_hhmmss'] = walk_hhmmss
        result['walk_ppm'] = walk_ppm
        result['miles'] = float(miles)

        if run_hhmmss and run_ppm and walk_hhmmss and walk_ppm and miles:
            run_duration_elapsed_time = ElapsedTime(run_hhmmss)
            run_ppm_elapsed_time = ElapsedTime(run_ppm)
            walk_duration_elapsed_time = ElapsedTime(walk_hhmmss)
            walk_ppm_elapsed_time = ElapsedTime(walk_ppm)
            distance = Distance(float(miles))
            mile = Distance(float(1.0))

            total_secs = float(run_duration_elapsed_time.secs +
                               walk_duration_elapsed_time.secs)
            run_pct = float(run_duration_elapsed_time.secs / total_secs)
            walk_pct = float(1.0 - run_pct)

            run_secs = float(run_pct * run_ppm_elapsed_time.secs)
            walk_secs = float(walk_pct * walk_ppm_elapsed_time.secs)
            avg_secs = float(run_secs + walk_secs)

            avg_time = ElapsedTime(avg_secs)
            avg_speed = Speed(mile, avg_time)

            result['avg_mph'] = avg_speed.mph()
            result['avg_ppm'] = avg_speed.pace_per_mile()
            result['proj_time'] = avg_speed.projected_time(distance)
            result['proj_miles'] = distance.as_miles()

        return result
