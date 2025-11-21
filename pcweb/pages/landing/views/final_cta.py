import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern


def content() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Secure Your Future with Singularity.",
            class_name="text-slate-12 lg:text-5xl text-3xl font-semibold text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "From Silicon to Satellite.",
            class_name="text-slate-11 text-lg text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.div(
            ui.link(
                render_=ui.button(
                    "Schedule Your Strategic Briefing",
                    size="lg",
                    class_name="font-semibold h-10",
                ),
                to="#schedule-briefing",
            ),
            ui.button(
                "Contact Sales / Schedule Demo",
                size="lg",
                variant="primary",
                class_name="font-semibold",
            ),
            class_name="flex flex-col sm:flex-row items-center gap-4 mt-8",
        ),
        class_name="flex flex-col items-center mx-auto w-full justify-center",
    )


def final_cta() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", reverse=True, class_name="left-0 top-0"),
        numbers_pattern(side="right", reverse=True, class_name="right-0 top-0"),
        content(),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20",
    )
